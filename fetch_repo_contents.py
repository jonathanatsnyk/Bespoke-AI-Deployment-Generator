# fetch_repo_contents.py

import requests
import json

def fetch_repo_contents(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        if response.text.strip():  # Check if response is not empty
            try:
                data = response.json()
                filenames = [item['name'] for item in data]

                # Save project type to a JSON file
                with open('project_type.json', 'w') as f:
                    json.dump({'data': data}, f)
                #print(filenames)
                return filenames
            except ValueError as e:
                print(f"Decoding JSON has failed for fetch repo contents. Error: {e}")
        else:
            print("Empty response received from server")
    else:
        print("Failed to fetch data, status code: ", response.status_code)
