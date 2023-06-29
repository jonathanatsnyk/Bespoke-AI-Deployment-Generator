import requests
import json

from AI_API import post_chat
from fetch_repo_contents import fetch_repo_contents
from dotenv import load_dotenv
import os
load_dotenv()

# Now you can access the variable


# github info
owner = "jonathanatsnyk"
repo = "juice-shop"
repo2 = "VulnerableApp"
token = os.getenv("GITHUB_TOKEN")



# ai_gateway

bearer_token = os.getenv("GATEWAY_BEARER_TOKEN")
url = "https://hackathon-gateway.c-a.eu-west-1.polaris-prod-bo-dr3d3-1.aws.snyk-internal.net"

filedata = fetch_repo_contents(owner, repo2, token)
filedata = ", ".join(str(i) for i in filedata)
post_chat(bearer_token, url, filedata)
