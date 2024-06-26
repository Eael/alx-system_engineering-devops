#!/usr/bin/python3
"""
Returns a TO-DO list for a given employee using REST API
"""
import requests
import sys


def to_do(id):
    """Script that displays employee TODO list
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

    for task in todos_json:
        if task.get("completed") is True:
            task_completed += 1
            task_list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          task_completed,
                                                          number_tasks))
    print(task_list[:-1])


if __name__ == '__main__':
    to_do(sys.argv[1])
