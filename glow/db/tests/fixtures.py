# Standard library
import uuid

# Third-party
import pytest

# Glow
import glow.db.db as db
from glow.db.models.run import Run
from glow.abstract_future import FutureState


@pytest.fixture(scope="function")
def test_db():
    original_db = db._db_instance
    temp_db = db.LocalDB("sqlite://")

    with open("glow/db/schema.sql", "r") as file:
        schema = file.read()

    connection = temp_db.get_engine().raw_connection()
    cursor = connection.cursor()
    cursor.executescript(schema)

    db._db_instance = temp_db

    try:
        yield temp_db
    finally:
        db._db_instance = original_db


@pytest.fixture
def run() -> Run:
    run = Run(
        id=uuid.uuid4().hex,
        future_state=FutureState.CREATED.value,
        name="test_run",
        calculator_path="path.to.test_run",
    )
    return run