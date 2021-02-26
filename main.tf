terraform {
  backend "local" {}
  required_providers {
    azuredevops = {
      source = "microsoft/azuredevops"
    }
  }
}

provider "azurerm" {
  features {}
}

variable "resource-group-name" {
  type = string
}

variable "azure-devops-project-name" {
  type = string
}

data "azuredevops_project" "project" {
  name = var.azure-devops-project-name
}

data "azurerm_subscription" "current" {
}
