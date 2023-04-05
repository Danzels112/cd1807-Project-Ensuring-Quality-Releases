# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time

def driver_all():
    print ('Starting the browser...')
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9515")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/danzels112/chromedriver')
    return driver

# Start the browser and login with standard_user
def login (driver, user, password):
    url = 'https://www.saucedemo.com/'
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get(url)
    username = driver.find_element(By.ID, 'user-name')
    print(f"Entering username {user}")
    username.send_keys(user)
    user_pw = driver.find_element(By.ID, 'password')
    print("Entering password")
    user_pw.send_keys(password)

    login_button = driver.find_element(By.ID, 'login-button')
    print("Submitting credentials to login")
    login_button.click()
    product_header = driver.find_element(By.CLASS_NAME, 'title')

    assert product_header.text == "Products", "ERROR: LOGIN FAILED"
    print("Login was successful")
    time.sleep(10)

def add_items(driver):
    items = []
    inventory_container = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    for item in inventory_container:
        item_name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
        items.append(item_name)
        item_description = item.find_element(By.CLASS_NAME, 'inventory_item_description')
        item_pricebar = item_description.find_element(By.CLASS_NAME, 'pricebar')
        item_button = item_pricebar.find_element(By.TAG_NAME,'button')
        item_button.click()
        print(f"Item {item_name} was added to shopping cart!")
        

    items_in_cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert int(items_in_cart) == len(items), "ERROR: ALL ITEMS NOT ADDED"
    print(f"Items expected {len(items)}, items in cart {items_in_cart}")
    time.sleep(10)

def del_items(driver):
    shopping_cart = driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    cart_container = driver.find_elements(By.CLASS_NAME, 'cart_item')
    for cart_item in cart_container:
        cart_item_name = cart_item.find_element(By.CLASS_NAME, 'inventory_item_name').text
        cart_label = cart_item.find_element(By.CLASS_NAME,'cart_item_label')
        cart_item_pricebar = cart_label.find_element(By.CLASS_NAME, 'item_pricebar')
        cart_item_button = cart_item_pricebar.find_element(By.TAG_NAME, 'button')
        cart_item_button.click()
        print(f"Item {cart_item_name} was removed from cart!")
        time.sleep(3)



if __name__ == "__main__":
    driver_to_use = driver_all()
    login(driver_to_use,'standard_user', 'secret_sauce')
    add_items(driver_to_use)
    del_items(driver_to_use)






