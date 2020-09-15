#!/usr/bin/python3
"""consume data from api"""


if __name__ == "__main__":
    import requests
    import sys
    arg = sys.argv[1]
    userId_request = requests.get(
        'https://jsonplaceholder.typicode.com/users?id=' +
        str(arg)).json()
    false_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' +
        str(arg) +
        '&completed=false').json()
    true_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' +
        str(arg) +
        '&completed=true').json()
    name = userId_request[0]["name"]
    done_task = len(true_todos)
    false_task = len(false_todos)
    total = done_task + false_task
    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          done_task, total))

    for task in true_todos:
        print('\t {}'.format(task["title"]))
