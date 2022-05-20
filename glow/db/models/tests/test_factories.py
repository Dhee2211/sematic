# Standard library
import hashlib
import json

# Glow
from glow.abstract_future import FutureState
from glow.calculator import calculator
from glow.db.models.factories import make_run_from_future, make_artifact
from glow.types.serialization import value_to_json_encodable, type_to_json_encodable


@calculator
def func():
    pass


def test_make_run_from_future():
    future = func()
    parent_future = func()
    future.parent_future = parent_future
    run = make_run_from_future(future)

    assert run.id == future.id
    assert run.future_state == FutureState.CREATED.value
    assert run.calculator_path == "glow.db.models.tests.test_factories.func"
    assert run.name == "func"
    assert run.parent_id == parent_future.id


def test_make_artifact():
    artifact = make_artifact(42, int)

    payload = {
        "value": value_to_json_encodable(42, int),
        "type": type_to_json_encodable(int),
    }

    sha1 = hashlib.sha1(json.dumps(payload, sort_keys=True).encode("utf-8"))

    assert artifact.id == sha1.hexdigest()
    assert artifact.json_summary == "42"