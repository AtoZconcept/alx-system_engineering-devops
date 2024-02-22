#!/usr/bin/python3
"""script to export data in the JSON format"""


import json
import requests
if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('{}/users/'.format(url)).json()

    dict_data = {}
    for user in users:
        user_id = user.get("id")
        todos = requests.get(url + '/users/{}/todos'.format(user_id)).json()

        task_list = []
        for task in todos:
            task_list.append(
                {"username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')}
            )
        dict_data[user_id] = task_list

    with open('todo_all_employees.json', 'w') as file:
        json.dump(dict_data, file)
