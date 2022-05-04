import json, os, requests

argocd_domain = os.environ['ARGOCD_DOMAIN']
argocd_app = os.environ['ARGOCD_APP']
project = os.environ['PROJECT_NAME']
environment = os.environ['ENVIRONMENT_NAME'] 
status = os.environ['DEPLOY_STATUS']

def send_message(argocd_domain: str, argocd_app: str, project: str, environment: str, status: str) -> bool:
  user = "SpaceX"
  argocd_link = f'https://{ argocd_domain }/applications/{ argocd_app }?resource='
  msg = f"""
  O Argo CD está tentando fazer deploy do *{ project }* no ambiente *{ environment }*. :rocket:
  Acompanhe a tentativa de deploy em { argocd_link }
  """

  icon_url = "https://ck-devops.s3.amazonaws.com/deploy-success-icon.png"

  if status == 'failure':
    user = "Houston, we have a problem!"
    msg = f"""
    O Argo CD falhou na tentativa de deploy do *{ project }* no ambiente *{ environment }*. :boom:
    Verifique o erro em { argocd_link }
    """

    icon_url = "https://ck-devops.s3.amazonaws.com/deploy-fail-icon.png"

  url = os.environ['SLACK_HOOK']
  data = json.dumps({
      "title": {
          "type": "plain_text",
          "text": "HealthCheck Fail"
      },
      "username": user,
      "text": msg,
      "icon_url": icon_url,
      "channel": "C01UT9Q6NJ0"
  })

  response = requests.post(url, data=data)
  print(f'Slack response {response.status_code}')
  if response.status_code == 200:
      return True
  
  return False

send_message(argocd_domain, argocd_app, project, environment, status)