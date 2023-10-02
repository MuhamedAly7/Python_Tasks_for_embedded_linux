import requests
import time
import json


def suggest_activity():
    try:
        # Sent GET request to the BoredAPI URL
        response = requests.get("https://www.boredapi.com/api/activity")

        # check if request is succesful or not
        if response.status_code == 200:
            data = response.json()
            activity = data.get("activity")
            print(f"\nyour activity suggestion : {activity}")

        else:
            print(f"failed to get an activity . status code {response.status_code}")

    except Exception as e:
        print("Error occured.")


print("Welcome to BoredAPI avtivity suggestion.\n")

while True:
    input("\nPress Enter to get new suggestion...")
    suggest_activity()
    user_input = input("\nDo you want another activity (y/n)")

    if user_input != "y":
        break