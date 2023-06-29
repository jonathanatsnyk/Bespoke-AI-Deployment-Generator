# api_call.py

import requests
import json

def post_chat(bearer_token, url, filedata):
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    # Read context from file
    with open("context.txt", "r") as file:
        context = file.read()

    data = {
        "provider": "openai",
        "model": "gpt-4",
        "model_input": {
            "context": context,
            "messages": [
                {
                    "role": "USER",
                    "content": filedata
                }
            ]
        }
    }

    response = requests.post(url + '/api/chat', headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        if response.text.strip():  # Check if response is not empty
            try:
                print(response.json())
                return response.json()
            except ValueError as e:
                print(f"Decoding JSON has failed for post chat. Error: {e}")
        else:
            print("Empty response received from server")
    else:
        print("Failed to fetch data for post chat, status code: ", response.status_code)
