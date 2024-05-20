#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format.
"""
import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user_url = ('https://jsonplaceholder.typicode.com'
                f'/users/{employee_id}')
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get('username')

    todos_url = (
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    )
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Failed to retrieve tasks")
        sys.exit(1)

    todos_data = todos_response.json()

    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get('completed'),
                task.get('title')
            ])

    print("Data exported to {}".format(csv_filename))
