from .data import data
from .models.task import Task

if __name__ == "__main__":
    print("####### App Started #######")
    input("Press Enter to Continue")

    print("####### Initializing Data Base #######")
    data.init_database()

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
        {
            "id": 3,
            "text": "This is a mistake",
            "day": "Sep 20th at 1:30pm",
            "reminder": False,
        },
    ]

    input("Press Enter to Continue")
    print("####### Inserting data #######")
    tasks = [Task(**document) for document in init_data]

    for task in tasks:
        data.insert_task(task)

    input("Press Enter to Continue")
    print("####### Deleting data #######")
    task = Task(id=3)
    data.delete_by_id(task)

    input("Press Enter to Continue")
    print("####### Validate data exists #######")

    read_tasks = data.get_all()

    assert tasks[0] in read_tasks
    assert tasks[1] in read_tasks
    assert tasks[2] not in read_tasks

    print("####### All validations PASSED #######")

    print("####### Finished #######")
