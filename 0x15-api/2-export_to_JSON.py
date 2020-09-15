#!/usr/bin/python3
"""consume data from api"""


if __name__ == "__main__":
    import requests
    import sys
    import json
    arg = sys.argv[1]
    userId_userName = requests.get(
        'https://jsonplaceholder.typicode.com/users?id=' +
        str(arg)).json()[0]["username"]
    todos_task = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(arg)).json()

    di = {str(arg): []}
    for el in todos_task:
        new = {
            "task": el["title"],
            "completed": el["completed"],
            "username": userId_userName}
        di[str(arg)].append(new)
    with open('{}.json'.format(arg), 'w') as f:
        f.write(json.dumps(di))
