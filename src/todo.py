tasks = []

def add_task(task_name, due_date):
    task = {"name": task_name, "due_date": due_date, "done": False}
    tasks.append(task)
    return task

def list_tasks():
    return tasks
