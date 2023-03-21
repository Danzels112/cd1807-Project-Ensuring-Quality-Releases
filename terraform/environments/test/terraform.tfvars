# Azure subscription vars
subscription_id = "601c9c7b-8f40-476f-92b1-3b437e0aef1d"
client_id = "14455a46-6089-4c3f-9310-7e89bf78d9ee"
client_secret = "" # THIS SHOULDN'T BE HARDCODED. Using ENV variable instead
tenant_id = "14ab4b19-a31c-4bd1-90af-caa984fe1312"

# Resource Group/Location
location = "East US"
resource_group = "Azuredevops"
application_type = "myApplication-xx"

# Network
virtual_network_name = ""
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"

# VM specific
vm_name = "azureDevops-linux"