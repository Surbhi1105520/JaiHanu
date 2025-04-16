import time
from selenium import webdriver
#webdriver is used to launch the browser then it will do other things
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/") # go driver and get and open a browser
time.sleep(3) # to skip the i am not a robot button

##input field
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Try logging in with a username
test_username = "standard_user"  # change this to test different usernames
test_password = "secret_sauce"   # password is the same for all users

username_input.send_keys(test_username)
password_input.send_keys(test_password)
login_button.click()
time.sleep(3) # wait for 3 seconds to see the result
# Check if login was successful
if "inventory.html" in driver.current_url:
    print(f"✅ Login successful for user: {test_username}")
else:
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
    print(f"❌ Login failed for user: {test_username}")
    print("Error:", error_msg)

driver.quit()