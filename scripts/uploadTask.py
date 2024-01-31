from dotenv import load_dotenv
import os
load_dotenv()
from openai import OpenAI
import requests
import typer
import json

app = typer.Typer()
client = OpenAI()
NOTION_API_KEY = os.environ["NOTION_API_KEY"]

class UploadTask:
  def __init__(self, databaseID):
    self.upload_note_to_notion(databaseID)

  def upload_note_to_notion(self, databaseID):
    url = f'https://api.notion.com/v1/databases/{databaseID}'
    headers = {
      'Authorization': f'Bearer {NOTION_API_KEY}',
      'Content-Type': 'application/json',
      'Notion-Version': '2022-06-28'
    }
    # data = {}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
      print("Get request successful")
    else:
      print(f"Get request failed with status code: {res.status_code}")
      return

    data = json.loads(res.text)
    print(data)
    return data["results"]

if __name__ == "__main__":
    databaseID = ""
    UploadTask(databaseID)
