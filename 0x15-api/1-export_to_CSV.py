#!/usr/bin/python3
"""consume data from api"""


if __name__ == "__main__":
    import requests
    import sys
    import csv
    arg = sys.argv[1]
    userId_request = requests.get(
        'https://jsonplaceholder.typicode.com/users?id=' +
        str(arg)).json()
    todos_task = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' +
        str(arg)).json()
    archivo = open('{}.csv'.format(arg), 'w')
    fields = ['userId', 'username', 'completed', 'title']
    csv_writer = csv.DictWriter(
        archivo,
        fieldnames=fields,
        quoting=csv.QUOTE_ALL)
    """csv_writer.writeheader()"""
    for el in todos_task:
        del el["id"]
        el["username"] = userId_request[0]["username"]
        csv_writer.writerow(el)
