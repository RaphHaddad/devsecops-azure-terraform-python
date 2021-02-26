# README

Example code referencing my blog post.

## Pre-requisites

- [Python](https://www.python.org)
- [Terraform](https://www.terraform.io)
- [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) if running on a Windows machine

## Authenticate to Platform

```cmd
% az login
The default web browser has been opened at https://login.microsoftonline.com/common/oauth2/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
% export AZDO_PERSONAL_ACCESS_TOKEN={a-secure-access-token}
% export AZDO_ORG_SERVICE_URL=https://dev.azure.com/{a-secure-org}
```

## Usage

```cmd
% ./setup-environment.py -h
usage: Setup environment [-h] --resource-group-name RESOURCE_GROUP_NAME --azure-devops-project-name AZURE_DEVOPS_PROJECT_NAME

optional arguments:
  -h, --help            show this help message and exit
  --resource-group-name RESOURCE_GROUP_NAME, -rg RESOURCE_GROUP_NAME
                        The resource group name to provission with the service connection.
  --azure-devops-project-name AZURE_DEVOPS_PROJECT_NAME, -pn AZURE_DEVOPS_PROJECT_NAME
                        The project name to where the service connection will be provisioned.
% ./setup-environment.py --resource-group-name "an-example-resource-group" --azure-devops-project-name main
...
...
...
Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
```
