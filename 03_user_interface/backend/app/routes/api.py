from typing import Union
from flask import Blueprint, jsonify, Response, request

from ..models.task import Task
from ..data import data

blueprint = Blueprint("api", __name__)


@blueprint.get("/tasks")
def get_all_tasks() -> Response:
    results = data.get_all()
    return jsonify([task._asdict() for task in results])


@blueprint.post("/tasks")
def insert_new_task() -> Response:
    task = request.get_json(force=True) or {}

    if "id" not in task:
        task["id"] = -1

    new_task = Task(**task)
    new_task = data.insert_task(new_task)
    return jsonify(new_task._asdict())


@blueprint.delete("/tasks/<id>")
def delete_tasks_by_id(id: Union[int, str]) -> Response:
    task = Task(id=int(id))
    data.delete_by_id(task)
    return jsonify({"Message": "OK"})
