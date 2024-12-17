import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from todo import add_task, list_tasks

def test_add_task():
    task = add_task("Buy groceries", "2024-12-20")
    assert task["name"] == "Buy groceries"
    assert task["due_date"] == "2024-12-20"
    assert task["done"] == False

def test_list_tasks():
    add_task("Buy groceries", "2024-12-20")
    tasks = list_tasks()
    assert len(tasks) > 0