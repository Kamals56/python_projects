
# task_storage.py
import json
from tasks import Task

def save_tasks(task_list):
    #Saves the tasks to a JSON file.
    with open("tasks.json", "w") as file:
        json.dump([task.to_dict() for task in task_list], file)

def load_tasks():
    #Loads the tasks from a JSON file.
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
        return [Task.from_dict(task) for task in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
