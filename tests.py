import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Testing(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        # Create a new instance of the Chrome driver and maximize the window
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(chrome_options)
        self.addCleanup(self.driver.quit)

    # teardown runs after each test case
    # def tearDown(self):
    #     self.driver.quit()
    #     ..and anything else needing teardown

    def test_form_6_celsius_fahrenheit_conversion(self):
        # Navigate to the website
        self.driver.get('http://localhost:8000/index.php?action=form6')

        # Validate a Celsius to Fahrenheit conversion
        self.driver.find_element(By.NAME, 'celsius').clear()
        self.driver.find_element(By.NAME, 'celsius').send_keys('30')

        wait = WebDriverWait(self.driver, 10)
        convert_btn = wait.until(ec.element_to_be_clickable((By.NAME, 'Convert')))
        convert_btn.click()

        expected_fahrenheit = '86'
        actual_fahrenheit = self.driver.find_element(By.NAME, 'fahrenheit').get_property('value')

        self.assertEqual(expected_fahrenheit, actual_fahrenheit,
                         "Expected value '" + expected_fahrenheit + "' but got '" + actual_fahrenheit + "'")

    def test_form_6_celsius_heading_text(self):
        # Navigate to the website
        self.driver.get('http://localhost:8000/index.php?action=form6')

        # expected_heading = "Sample Heading"
        expected_heading = "Form 6 - Convert Celsius to Fahrenheit"
        actual_heading = self.driver.find_element(By.TAG_NAME, "h2").text

        self.assertEqual(expected_heading, actual_heading,
                         "Expected heading '" + expected_heading + "' but got '" + actual_heading + "'")


if __name__ == '__main__':
    unittest.main()
