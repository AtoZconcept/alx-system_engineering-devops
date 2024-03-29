#!/usr/bin/python3
"""Python sripts that returns information about his/her TODO list progress"""


import requests
import sys
if __name__ == "__main__":
    """returns information about his/her TODO list progress"""
    if len(sys.argv) != 2:
        print('Usage: sys.argv[0] <employee_id>')
        sys.exit(1)

    employee_id = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + '/users/{}'.format(employee_id)).json()
    todos = requests.get(url + '/users/{}/todos'.format(employee_id)).json()

    completed_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed_tasks), total_tasks)
        )
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
