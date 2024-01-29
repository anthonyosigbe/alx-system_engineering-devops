#!/usr/bin/python3
"""Retrieve data from an API and export it in CSV format.
"""
import csv
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
    filename = '{emp_id}.csv'.format(emp_id=emp_id)

    # User Response
    res = requests.get(user_uri).json()

    # Username of the employee
    username = res.get('username')

    # User TODO Response
    res = requests.get(todo_uri).json()

    # Create the new file for the user to save the information
    # Filename example: `{user_id}.csv`
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in res:
            # Completed or non-completed task
            status = elem.get('completed')

            # The task name
            title = elem.get('title')

            # Writing each result of API response in a row of a CSV file
            writer.writerow([emp_id, username, status, title])
