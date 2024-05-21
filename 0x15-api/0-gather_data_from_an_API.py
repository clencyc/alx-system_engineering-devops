#!/usr/bin/python3

"""Gathering data form an API"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    url = f'https://jsonplaceholder.typicode.co/todos?userId={employee_id}'

    response = requests.get(url)
    if response.status_code != 200:
        print("Error":, response.text)
        return

        todo_list = response.json()
        total_tasks = len(todo_list)
        completed_tasks = sum(1 for task in todo_list if task['completed'])
        employee_name = todo_list[0]['name']

         print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
         for task in todo_list:
             if task['completed']:
                 print(f"\t{task['title']}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

        employee_id = int(sys.argv[1])

        get_employee_todo_progress(employee_id)
