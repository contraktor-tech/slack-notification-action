# Slack Notification Action

[![Quality Gate Status](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=alert_status&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Bugs](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=bugs&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Vulnerabilities](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=vulnerabilities&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Code Smells](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=code_smells&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Coverage](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=coverage&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)
[![Lines of Code](https://sonar.contraktor.com.br/api/project_badges/measure?project=contraktor-tech_slack-notification-action&metric=ncloc&token=8731a24f1942601cd9a8778b04086650dd4d7795)](https://sonar.contraktor.com.br/dashboard?id=contraktor-tech_slack-notification-action)

This action was created to send notifications to Slack

```yaml
inputs:
  slack-hook:
    description: 'token connect Slack'
    require: true
  argocd-domain:
    description: 'domain intern of Argo CD'
    require: true
  argocd-app:
    description: 'application name at Argo CD'
    require: true 
  project-name:
    description: 'project deploy'
    require: true
  environment-name:
    description: 'environment to project deploy'
    require: true
  deploy-status:
    description: 'deploy status'
    require: true
```
