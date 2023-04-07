import os 
import requests

from dotenv import load_dotenv # TODO: Remove
load_dotenv() # TODO: Remove

# Call GitHub API and retrieve issues
repo = "https://api.github.com/repos/SeanBannister/test/"
headers = {"Authorization": "Bearer" + os.getenv("GITHUB_TOKEN")}
response = requests.get(repo + "issues", headers=headers)

# Print out the latest issues body text
if response.status_code == 200:
    # Pretty print the latest issues
    print(response.json()[0]["body"])
