#!/usr/bin/python3
"""Script uses this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv

if (len(argv) == 2) and int(argv[1]):
    response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(argv[1]))
    name = response.json()['name']

    response = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(argv[1]))
    todos = response.json()
    totalTodos = 0
    doneTodos = 0
    titleTab = "\t "
    task_titles = ""

    for todo in todos:
        if todo['completed']:
            doneTodos += 1
            task_titles += titleTab + todo['title'] + "\n"
        totalTodos += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, doneTodos, totalTodos))
    print(task_titles, end="")
