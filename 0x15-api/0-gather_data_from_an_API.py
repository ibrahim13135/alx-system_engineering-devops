#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python3 {} employee_id".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    # Fetching employee info
    user_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    todos_response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id))

    if user_response.status_code != 200:
        print("User not found")
        exit(1)

    if todos_response.status_code != 200:
        print("TODOs not found")
        exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    # Calculating TODO progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for task in todos_data if task['completed'])

    # Displaying progress
    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], done_tasks, total_tasks))
    for task in todos_data:
        if task['completed']:
            print("\t{}".format(task['title']))
