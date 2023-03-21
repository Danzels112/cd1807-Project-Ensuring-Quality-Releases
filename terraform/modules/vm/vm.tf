resource "azurerm_network_interface" "linux_box_nic" {
  name                = "${var.vm_name}-nic"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip}"
  }
}

data "azurerm_image" "packer_custom"{
    resource_group_name = "Azuredevops"
    name                = "lin-img-test-image-20230320172548"
}

resource "azurerm_linux_virtual_machine" "linux_box" {
  name                = "${var.vm_name}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  disable_password_authentication = false
  admin_username      = "danzels112"
  admin_password = "admin@123!"
  network_interface_ids = [azurerm_network_interface.linux_box_nic.id]
  source_image_id = data.azurerm_image.packer_custom.id

  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
}
