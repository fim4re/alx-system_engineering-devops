#!/usr/bin/python3
"""Exports information of all employees to JSON"""
import json
import requests

if __name__ == "__main__":
    # Fetch user information and to-do lists
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    # Create a dictionary containing to-do list
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
