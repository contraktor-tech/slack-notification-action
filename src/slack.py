import json, os, requests

project = os.environ['PROJECT_NAME']
environment = os.environ['ENVIRONMENT_NAME'] 
status = os.environ['DEPLOY_STATUS']

def send_message(project: str, environment: str, status: str) -> bool:
  if status == 'success':
    user = "Spacex"
    msg = f"Deploy do projeto '{ project }' do ambiente '{ environment }' concluído com sucesso.   :rocket:"
    icon_url = "https://ck-devops.s3.amazonaws.com/rocket-icon.png"
  else:
    user = "Houston, we have a problem!"
    msg = f"Tem que ver isso ae, talkei. Projeto '{ project }' do ambiente '{ environment }' falhou.  :boom:"
    icon_url = "https://ck-devops.s3.amazonaws.com/deploy-fail-icon.jpg"

  url = os.environ['SLACK_HOOK']
  data = json.dumps({
      "title": {
          "type": "plain_text",
          "text": "HealthCheck Fail"
      },
      "username": user,
      "text": msg,
      "icon_url": icon_url,
      "channel": "C037Q3ZEYPM"
  })

  response = requests.post(url, data=data)
  print(f'Slack response {response.status_code}')
  if response.status_code == 200:
      return True
  
  return False

send_message(project, environment, status)