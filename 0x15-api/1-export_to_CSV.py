#!/usr/bin/python3
"""Script uses this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import csv
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

    # csv write
    filename = userId + ".csv"
    with open(filename, mode='w') as todo_file:
        todo_writer = csv.writer(todo_file, delimiter=',',
                                 quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            todo_writer.writerow([userId, name,
                                 todo['completed'], todo['title']])
