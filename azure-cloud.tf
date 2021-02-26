resource "azurerm_resource_group" "resource-group" {
  name     = var.resource-group-name
  location = "Australia East"
}

resource "azurerm_role_assignment" "resource-group-service-principle-role-assignment" {
  scope                = azurerm_resource_group.resource-group.id
  role_definition_name = "Contributor"
  principal_id         = azuread_service_principal.service-principle.id
}

resource "azuread_application" "ad-application" {
  display_name = "${var.resource-group-name}-spn"
}

resource "azuread_service_principal" "service-principle" {
  application_id               = azuread_application.ad-application.application_id
}

resource "azuread_service_principal_password" "service-principle-password" {
  service_principal_id = azuread_service_principal.service-principle.id
  description          = "Managed by Terraform"
  value                = random_password.service-principle-password.result
  end_date             = "2099-01-01T01:02:03Z"
}

resource "random_password" "service-principle-password" {
  length           = 16
  special          = true
  override_special = "_%@"
}
