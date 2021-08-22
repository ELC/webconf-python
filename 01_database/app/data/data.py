from typing import List
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
    with database_connection() as db:
        db.truncate()
        db.default_table_name = "tasks"


def insert_task(task: Task) -> Task:
    task_dict = task._asdict()

    if task.id == -1:
        all_tasks = get_all()
        last_task = max(all_tasks, key=lambda x: x.id)
        task_dict["id"] = last_task.id + 1

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
