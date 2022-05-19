# Slack Notification Action

[![Quality Gate Status](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=alert_status&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Bugs](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=bugs&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Vulnerabilities](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=vulnerabilities&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Code Smells](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=code_smells&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Coverage](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=coverage&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Lines of Code](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=ncloc&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)

Action que envia notificação de status de deploy para o Slack.

## Inputs
Todos os inputs são de definição obrigatória.

- **slack-hook** → token de acesso do Slack
- **argocd-domain** → dominío interno do ArgoCD
- **argocd-app** → nome da aplicação no ArgoCD
- **project-name** → aplicação
- **environment-name** → ambiente
- **deploy-status** → status do deploy

## Etapas
- Verifica se o Python está instalado
- Instala as dependencias
- Executa o script e envia a notificação para o Slack

## Como usar
Acesse a documentação no [Confluence](https://contraktor.atlassian.net/wiki/spaces/CONTRAKTOR/pages/16842753/Actions#%3Aslack_icon%3A-slack-notification-action) para ver uma pipeline de exemplo.

- **sucesso no envio para deploy**
```
- name: deploy has succeeded - Send notification deploy to Slack
  uses: contraktor-tech/slack-notification-action@v1
  if: ${{ success() }}
  with:
    slack-hook: XXXX
    argocd-domain: XXXX
    argocd-app: XXXX
    project-name: XXXX
    environment-name: XXXX
    deploy-status: 'success'
```

- **falha no envio para deploy**
```
- name: deploy has failed - Send notification deploy to Slack
  uses: contraktor-tech/slack-notification-action@v1
  if: ${{ failure() }}
  with:
    slack-hook: XXXX
    argocd-domain: XXXX
    argocd-app: XXXX
    project-name: XXXX
    environment-name: XXXX
    deploy-status: 'failure'
```