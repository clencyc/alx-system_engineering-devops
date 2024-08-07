#!/usr/bin/python3

"""Gathering data from an API"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    params = {"userId":employee_id}

    todos_response = requests.get(url + "/todos", params=params)
    todos = todos_response.json()
    completed = []
    for todo in todos:
        if todo.get("competed"):
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".format(user.get("name"), len(completed), len(todo)))

    for complete in completed:
        print("t {}".format(complete))
