#!/usr/bin/python3
"""Script uses this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
user_data = response.json()
complete_user_data = dict()

for user in user_data:
    userId = user['id']
    username = user['username']

    response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(userId))
    todos = response.json()

    complete_user_data[userId] = []   # creates object of each user
    for todo in todos:
        det_dict = {"username": username,
                    "task": todo['title'],
                    "completed": todo['completed']}
        complete_user_data[userId].append(det_dict)

    todo_object = json.dumps(complete_user_data)

    filename = "todo_all_employees.json"
    with open(filename, 'w') as todo_json:
        todo_json.write(todo_object)
