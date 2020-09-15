#!/usr/bin/python3
"""consume data from api"""


if __name__ == "__main__":
    import requests
    import json
    len_users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    users = [(el["username"], el["id"]) for el in len_users]
    end_dict = {}
    for username, user_id in users:
        empty_dict = {}
        todos_task = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.
            format(user_id)).json()
        user_list_task = []
        for el in todos_task:
            new = {
                "username": username,
                "task": el["title"],
                "completed": el["completed"]
            }
            user_list_task.append(new)
        end_dict[str(user_id)] = user_list_task
    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(end_dict))
