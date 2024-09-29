import time
import unittest

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
# expected_heading = "Sample Heading"
expected_heading = "Form 6 - Convert Celsius to Fahrenheit"
actual_heading = driver.find_element(By.TAG_NAME, "h2").text

# The actual assertion
tc = unittest.TestCase()
tc.assertEqual(expected_heading, actual_heading, "Expected heading '" + expected_heading + "' but got '" + actual_heading + "'")


# Close the browser, after 2.5 seconds. If assertion above fails browser closes immediately.
time.sleep(2.5)
driver.quit()
