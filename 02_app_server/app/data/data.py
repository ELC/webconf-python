from typing import List, Optional
from pathlib import Path

from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage

from contextlib import contextmanager

from ..models.task import Task


CURRENT_DIRECTORY = Path(__file__).resolve().parent
DATABASE_PATH = Path(CURRENT_DIRECTORY, "db.json")

DATABASE_PARAMS = dict(storage=JSONStorage, indent=4, separators=(",", ": "))


@contextmanager
def database_connection():
    db = TinyDB(DATABASE_PATH, **DATABASE_PARAMS)
    db.default_table_name = "tasks"

    try:
        yield db
    finally:
        db.close()


def init_database():
    init_data = [
        {
            "id": 1,
            "text": "Doctors Appointment",
            "day": "Feb 5th at 2:30pm",
            "reminder": True,
        },
        {
            "id": 2,
            "text": "Meeting at School",
            "day": "Feb 6th at 1:30pm",
            "reminder": True,
        },
    ]

    with database_connection() as db:
        db.truncate()
        db.default_table_name = "tasks"

    for document in init_data:
        task = Task(**document)
        insert_task(task)


def insert_task(task: Task) -> Task:
    task_dict = task._asdict()

    if task.id == -1:
        new_id = max(get_all(), key=lambda x: x.id).id + 1
        task_dict["id"] = new_id

    with database_connection() as db:
        db.insert(task_dict)

    return Task(**task_dict)


def get_all() -> List[Task]:
    with database_connection() as db:
        results = db.all()
    return [Task(**task) for task in results]


def delete_by_id(task: Task) -> None:
    Task_ = Query()

    with database_connection() as db:
        db.remove(Task_.id == task.id)
