provider "azurerm"{
version = '=2.4.0
feature{}
}
resource "azure_resource_group" "example" {
name     =  "example'
location   = "East US"
}
output "id"{
     value  = data.azurerm_resource_group.example.id
}