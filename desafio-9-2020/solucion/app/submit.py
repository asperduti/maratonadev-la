import json
import requests
from logging import info


def submit(token):
    # Submits the user data for validation
    url = "http://172.21.86.186:5000/submit"
    with open('./data.json', 'r') as d:
        j = json.load(d)

        j['submit_confirmation'] = True
        j['iam_token'] = token

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        res = requests.post(url, json=j, headers=headers)

        info(res.json())

