resource "azuredevops_serviceendpoint_azurerm" "serviceendpoint-azure" {
  project_id            = data.azuredevops_project.project.id
  service_endpoint_name = "${var.resource-group-name}-azure-service-connection"
  description = "Managed by Terraform" 
  credentials {
    serviceprincipalid  = azuread_service_principal.service-principle.id
    serviceprincipalkey = random_password.service-principle-password.result
  }
  azurerm_spn_tenantid      = data.azurerm_subscription.current.tenant_id
  azurerm_subscription_id   = data.azurerm_subscription.current.subscription_id
  azurerm_subscription_name = data.azurerm_subscription.current.display_name
}
