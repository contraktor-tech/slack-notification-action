# Slack Notification Action

This action was created to send notifications to Slack

```yaml
inputs:
  slack-hook:
    description: 'token connect Slack'
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