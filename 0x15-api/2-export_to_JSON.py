#!/usr/bin/python3
"""Retrieve data from an API and export it in JSON format.
"""
from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    # Verifies whether the argument is convertible to a number.
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    # Convert main formatted names into API URIs and filenames.
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.json'.format(emp_id=emp_id)

    # User Response
    user_res = requests.get(user_uri).json()

    # User TODO Response
    todo_res = requests.get(todo_uri).json()

    # A list of all tasks of an user
    user_tasks = list()

    for elem in todo_res:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': user_res.get('username')
        }

        user_tasks.append(data)

    # Create the new file for the user to save the information
    # Filename example: `{user_id}.json`
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({emp_id: user_tasks}))
