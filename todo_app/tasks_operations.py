# task_operations.py
from tasks import Task

def add_task(task_list, title):
    task = Task(title)
    task_list.append(task)
    return task

def remove_task(task_list, title):
    for task in task_list:
        if task.title == title:
            task_list.remove(task)
            return True
    return False

def list_tasks(task_list):
    return [task.to_dict() for task in task_list]
