import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Create a new instance of the Chrome driver and maximize the window
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(chrome_options)

# Navigate to the website
driver.get("http://localhost:8000/index.php?action=form6")

# We wait for the Convert button to be clickable
wait = WebDriverWait(driver, 10)
element = wait.until(ec.element_to_be_clickable((By.NAME, 'Convert')))

# Validate the main header
expected_heading = "Bug Report Form"
actual_heading = driver.find_element(By.TAG_NAME, "h2").text

if expected_heading == actual_heading:
    print("Header validation successful!")
else:
    print("Header validation failed. Expected:", expected_heading, "Actual:", actual_heading)

time.sleep(2.5)

# Close the browser
driver.quit()
