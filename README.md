# Python Selenium Example

## Application under Test
The tests were written for https://github.com/andreasneuber/automatic-test-sample-site.  
README in that repo has further details how to set it up.

## Setup for Windows
- Get Chromedriver for example with https://github.com/andreasneuber/update-chromedriver
- Include the directory with the Chromedriver executable in your systems PATH variable
- Clone this repo
- In [PyCharm IDE](https://www.jetbrains.com/pycharm/) click on interpreter info (usually) displayed in bottom right corner  
- Add New Interpreter > Add Local Interpreter... > Virtualenv Environment: New > OK  
- `.venv/Scripts/activate`
- `pip install -r requirements.txt`

## Execute the tests
`py tests.py`
