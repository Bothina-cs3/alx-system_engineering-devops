#!/usr/bin/python3
"""
using this REST API, for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    if sys.argv[1].isdigit():
        employee_id = int(sys.argv[1])
    else:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = f'{REST_API}/users/{employee_id}'
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_data = user_response.json()

    todos_url = f'{REST_API}/todos'
    todos_response = requests.get(todos_url, params={'userId': employee_id})

    if todos_response.status_code != 200:
        print("Failed to retrieve tasks")
        sys.exit(1)

    todos_data = todos_response.json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
