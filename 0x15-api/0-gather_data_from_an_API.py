#!/usr/bin/python3
"""Returns a TO-DO list for a given employee using REST API"""
import requests
import sys


def to_do(id):
    """Script that displays employee TODO list
        Parameters:
        id: an integer representing employee id
    """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    todos = requests.get(url + "todos", params={"userId": id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]


if __name__ == '__main__':
    to_do(sys.argv[1])
