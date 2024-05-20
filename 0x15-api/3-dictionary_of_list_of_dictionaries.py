#!/usr/bin/python3
"""Exports to-do list information employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command-line
    user_id = sys.argv[1]
    # Fetch the list of all users
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Create a dictionary containing to-do list
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
