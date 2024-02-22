#!/usr/bin/python3
"""script to export data in the JSON format"""


import json
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ', sys.argv[0], '<employee id>')
        sys.exit(1)

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + '/users/{}'.format(user_id)).json()
    todos = requests.get(url + '/users/{}/todos'.format(user_id)).json()

    task_list = []
    for task in todos:
        if task.get('userId') == int(user_id):
            task_list.append(
                {"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.get('username')}
            )
        json_data = {user_id: task_list}
    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(json_data, file)
