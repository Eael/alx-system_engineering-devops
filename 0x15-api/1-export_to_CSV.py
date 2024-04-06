#!/usr/bin/python3
"""
Exports all tasks that are owned by this employee to CSV
"""
import requests
import sys


def to_do(id):
    """Script that exports employiee tasks to CSV file
        Parameters:
        id: an integer representing employee id
    """
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json["name"]

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    number_tasks = len(todos_json)

    task_completed = 0
    task_list = ""

    filename = "{}.csv".format(id)

    with open(filename, "w") as csvfile:
        for todo in todos_json:
            completed = todo.get("completed")
            title = todo.get("title")
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(id, employee_name,
                                                            completed, title)
            csvfile.write(csv_data)


if __name__ == '__main__':
    to_do(sys.argv[1])
