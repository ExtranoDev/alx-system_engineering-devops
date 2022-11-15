#!/usr/bin/python3
"""Script uses this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import json
import requests
from sys import argv

if (len(argv) == 2) and int(argv[1]):
    userId = argv[1]
    response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(userId))
    name = response.json()['username']

    response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(userId))
    todos = response.json()
    todos_dict = {userId: []}

    for todo in todos:
        det_dict = {"task": todo['title'],
                    "completed": todo['completed'],
                    "username": name}
        todos_dict[userId].append(det_dict)

    todo_object = json.dumps(todos_dict)

    filename = userId + ".json"
    with open(filename, 'w') as todo_json:
        todo_json.write(todo_object)
