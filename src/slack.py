import json, os, requests

project = os.environ['PROJECT_NAME']
environment = os.environ['ENVIRONMENT_NAME'] 

def send_message(project: str, environment: str ) -> bool:
  msg = ( f"Deploy of project { project } of environment { environment } completed.   :rocket:" )
  url = os.environ['SLACK_HOOK']
  data = json.dumps({
      "title": {
          "type": "plain_text",
          "text": "HealthCheck Fail"
      },
      "username": "Deploy Notification",
      "text": msg,
      "icon_url": "https://ck-devops.s3.amazonaws.com/rocket-icon.png",
      "channel": "C037Q3ZEYPM"
  })

  response = requests.post(url, data=data)
  print(f'Slack response {response.status_code}')
  if response.status_code == 200:
      return True
  
  return False

send_message()