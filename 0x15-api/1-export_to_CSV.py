#!/usr/bin/python3
"""Exports information employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from the command-line
    user_id = sys.argv[1]

    # Define the base URL for the JSON
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Use list comprehension to iterate over the to-do list
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
