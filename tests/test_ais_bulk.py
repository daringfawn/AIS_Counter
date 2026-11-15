"""The AIS routes with a bulk version (bulk=True in app/routes/ais.py): one
request runs the single route once per item, with that route's own checks
and words, and one item failing does not stop the rest."""
from __future__ import annotations

import json

import pytest

from app.models import ais, users
from app.routes.mcp_tools import build_registry
from app.routes.mcp_tools_ais import BULK_TOOLS
from tests.test_batches import LINE, P, files, row
from tests.test_matlab_routes import Harness


@pytest.fixture
def h(tmp_path):
    return Harness(tmp_path)


def post(h, path, who, **body):
    response = h.get("POST", path, session=who, body=body)
    return response.status, json.loads(response.data)


def batch_for(h, who, name="f"):
    return ais.create_batch(h.store, name, "upload", files((f"{name}/a" + P, name + "a")), who.id)


def outcomes(reply):
    return [(result["ok"], result.get("status")) for result in reply["results"]]


def test_results_are_deleted_each_on_its_own(h):
    ann, bea = h.user("Ann"), h.user("Bea")
    batch = batch_for(h, ann)
    mine = [ais.add_result(h.store, batch["id"], "a", row(), ann.id) for _ in range(3)]
    theirs = ais.add_result(h.store, batch_for(h, bea, "g")["id"], "a", row(), bea.id)
    items = [{"result_id": mine[0]["id"]}, {"result_id": 9999}, {"result_id": theirs["id"]},
             {"result_id": mine[1]["id"], "expect": 7}, {"result_id": mine[2]["id"]}]
    status, reply = post(h, "/api/bulk/ais/results/delete", ann, items=items)
    assert status == 200, reply
    assert outcomes(reply) == [(True, None), (False, 404), (False, 403), (False, 409), (True, None)]
    assert (reply["done"], reply["failed"]) == (2, 3)
    assert reply["results"][2]["error"] == "only whoever accepted it, the image's assignee, or an admin, can delete it"
    assert [r["id"] for r in ais.list_results(h.store, batch["id"])] == [mine[1]["id"]]
    assert reply["results"][4]["reply"]["ok"] is True


def test_results_and_lines_are_updated_with_shared_fields(h):
    ann = h.user()
    batch = batch_for(h, ann)
    first, second = (ais.add_result(h.store, batch["id"], "a", row(), ann.id) for _ in range(2))
    status, reply = post(h, "/api/bulk/ais/results/update", ann,
                         items=[{"result_id": first["id"]}, {"result_id": second["id"], "row": row(3.0)}],
                         shared={"row": row(2.0)})
    assert (status, reply["done"]) == (200, 2), reply
    assert [r["length_um"] for r in ais.list_results(h.store, batch["id"])] == [2.0, 3.0]

    line = ais.add_measurement(h.store, batch["id"], "a", LINE, ann.id)
    status, reply = post(h, "/api/bulk/ais/measurements/update", ann,
                         items=[{"measurement_id": line["id"], "measurement": LINE | {"label": "x"}}])
    assert (status, reply["done"]) == (200, 1), reply
    status, reply = post(h, "/api/bulk/ais/measurements/delete", ann,
                         items=[{"measurement_id": line["id"]}, {"measurement_id": line["id"]}])
    assert outcomes(reply) == [(True, None), (False, 404)]


def test_batches_archive_done_and_assign_in_bulk(h):
    ann, bea = h.user("Ann"), h.user("Bea")
    admin = h.user("Cy", role=users.ROLE_ADMIN)
    a, b = batch_for(h, ann, "f"), batch_for(h, ann, "g")
    other = batch_for(h, bea, "k")
    status, reply = post(h, "/api/bulk/ais/batches/archive", ann,
                         items=[{"batch_id": a["id"]}, {"batch_id": b["id"]}, {"batch_id": other["id"]}],
                         shared={"archived": True})
    assert outcomes(reply) == [(True, None), (True, None), (False, 403)], reply
    assert [ais.get_batch(h.store, x["id"]).get("archived_at") is not None for x in (a, b, other)] == [True, True, False]

    status, reply = post(h, "/api/bulk/ais/batches/done", ann,
                         items=[{"batch_id": a["id"], "image": "a"}, {"batch_id": a["id"], "image": "nope"}],
                         shared={"done": True})
    assert outcomes(reply) == [(True, None), (False, 400)], reply

    shares = [{"user_id": ann.id, "percent": 100}]
    assert post(h, "/api/bulk/ais/batches/assign", ann, items=[{"batch_id": a["id"], "shares": shares}])[0] == 403
    status, reply = post(h, "/api/bulk/ais/batches/assign", admin,
                         items=[{"batch_id": a["id"]}, {"batch_id": 9999}], shared={"shares": shares})
    assert outcomes(reply) == [(True, None), (False, 404)], reply


def test_batches_go_to_the_trash_and_back_in_bulk(h):
    ann = h.user("Ann")
    admin = h.user("Cy", role=users.ROLE_ADMIN)
    a, b = batch_for(h, ann, "f"), batch_for(h, ann, "g")
    ais.add_result(h.store, a["id"], "a", row(), ann.id)
    status, reply = post(h, "/api/bulk/ais/batches/delete", ann, items=[{"batch_id": a["id"]}, {"batch_id": b["id"]}])
    assert (status, reply["done"]) == (200, 2), reply
    trash = [result["reply"]["trash_id"] for result in reply["results"]]

    status, reply = post(h, "/api/bulk/ais/trash/restore", ann, items=[{"trash_id": trash[0]}, {"trash_id": 9999}])
    assert outcomes(reply) == [(True, None), (False, 404)], reply
    assert len(ais.list_results(h.store, a["id"])) == 1

    assert post(h, "/api/bulk/ais/trash/purge", ann, items=[{"trash_id": trash[1]}])[0] == 403
    status, reply = post(h, "/api/bulk/ais/trash/purge", admin, items=[{"trash_id": trash[1]}, {"trash_id": trash[1]}])
    assert outcomes(reply) == [(True, None), (False, 404)], reply


def test_a_reset_in_bulk_is_for_admins(h):
    ann = h.user("Ann")
    admin = h.user("Cy", role=users.ROLE_ADMIN)
    a = batch_for(h, ann)
    ais.add_result(h.store, a["id"], "a", row(), ann.id)
    assert post(h, "/api/bulk/ais/batches/reset", ann, items=[{"batch_id": a["id"]}], shared={"scope": "all"})[0] == 403
    status, reply = post(h, "/api/bulk/ais/batches/reset", admin, items=[{"batch_id": a["id"]}], shared={"scope": "all"})
    assert (status, reply["results"][0]["reply"]["deleted"]) == (200, 1), reply


def test_the_body_is_checked_as_a_whole_and_needs_the_csrf_token(h):
    ann = h.user()
    assert post(h, "/api/bulk/ais/results/delete", ann, items=[])[0] == 400
    assert post(h, "/api/bulk/ais/results/delete", ann, items=[{"result_id": 1}] * 101)[0] == 400
    assert post(h, "/api/bulk/ais/batches/archive", ann, items=[{"batch_id": 1}], shared={"nope": 1})[0] == 400
    response = h.get("POST", "/api/bulk/ais/results/delete", extra=((b"cookie", ann.cookie.encode()),),
                     raw=json.dumps({"items": [{"result_id": 1}]}).encode())
    assert response.status == 403


def test_the_bulk_tools_are_the_ones_named():
    names = {tool.name for tool in build_registry().tools()}
    assert {name + "_bulk" for name in BULK_TOOLS} <= names
    for kept_out in ("reset_batch_auto_bulk", "delete_batch_bulk", "restore_from_trash_bulk"):
        assert kept_out not in names
