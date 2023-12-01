### get sentiment data ###

# fuck this, it doesn't work #

from scrapingbee import ScrapingBeeClient
import os

MAIN_URL = "https://n.rivals.com/users/sign_in"

# connect to scraping provider
scraping_bee_key = os.environ.get("scraping_bee_key")
client = ScrapingBeeClient(api_key=scraping_bee_key)

response = client.get(
    MAIN_URL,
    params= {
        "country_code": "us",
        "js_scenario": {"instructions":[
            {"fill": [str('//*[@id=' + '"' + '"' + '__next' + '"' + ']/main/div/div/div/div/div[1]/form/div[1]/label/input'), "GoneWest1"]}, # Enter registration email
            {"fill": [str('//*[@id="' + '__next"' + ']/main/div/div/div/div/div[1]/form/div[2]/div/label/input'), "He@ven123"]}, # Enter password
            {"click": str('//*[@id=' + '"__next"' + ']/main/div/div/div/div/div[1]/form/div[3]/button')}, # Click on login
            {"wait": 1000} # Wait for a second
        ]},
        "screenshot_full_page": True # Take a screenshot
    }
)

if response.ok:
    with open("./screenshot.png", "wb") as f:
        f.write(response.content)
else:
    print(response.content)


###########################

import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the login page
login_url = "https://n.rivals.com/users/sign_in"
session = requests.Session()
response = session.get(login_url)

# Step 2: Parse the HTML (optional)
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# Step 3: Prepare the login data
login_data = {
    'username': 'GoneWest1',
    'password': 'He@ven123',
    'csrf_token': csrf_token  # if required
}

# Step 4: Send a POST request to authenticate
login_response = session.post(login_url, data=login_data)

# Step 5: Check the login response
if login_response.status_code == 200:
    print("Login successful")
else:
    print("Login failed")

response = session.get('https://texastech.forums.rivals.com/threads/texas-tech-v-texas-a-m-corpus-christi-pres-by-energy-renovation-center.185727/')


#####################

import requests
from bs4 import BeautifulSoup

# Start a session
session = requests.Session()

# Get the login page
login_page = session.get("https://n.rivals.com/users/sign_in")
login_html = BeautifulSoup(login_page.content, 'html.parser')

# Find the CSRF token or other necessary hidden fields
#csrf_token = login_html.find('input', {'name': 'csrf_token'})['value']

# Create the payload with the necessary login details
payload = {
    'login': 'GoneWest1',
    'password': 'He@ven123',
}

# Post the login request
login_response = session.post('https://n.rivals.com/users/sign_in', data=payload)

# Check if login was successful
if "Login successful" in login_response.text:
    print("Logged in!")
else:
    print("Failed to log in.")

base_url = 'https://texastech.forums.rivals.com/threads/texas-tech-v-kansas-pres-by-js-salsa-ttu-wins-16-13.185484/'

base_url_response = session.get(base_url)

print(base_url_response.text)




######################

import os
from time import sleep
import pandas
import datetime
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
chromedriver_autoinstaller.install()

def get_new_options():
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--mute-audio")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")
    options.page_load_strategy='eager'
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-popup-blocking')
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    return options
product_link=input('Enter your product link : ')
driver =webdriver.Chrome(options=get_new_options())
driver.maximize_window()
driver.get('https://n.rivals.com/users/sign_in')
sleep(2)
driver.find_element(By.XPATH,'//input[@name="login"]').send_keys('CJK5Hookers')
sleep(1)
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('cjk5hcjk5hc')
sleep(1)
driver.find_element(By.XPATH,'//button[@class="Button_button___KSka Button_medium__N5gPS"]').click()
sleep(10)
driver.get(product_link)
sleep(100)

#######

from webbot import Browser
from bs4 import BeautifulSoup
import time

web = Browser()
web.go_to('https://texastech.rivals.com/users/sign_in')
#enter your username and password in the into fields below
web.type('CJK5Hookers', into='login')
web.type('cjk5hcjk5hc', into='password')
web.click('Log In', tag='span')
time.sleep(5)

content = web.get_page_source()
soup = BeautifulSoup(content)

#You can now find the element you want
samples = soup.find_all("a", "item-title")


#############

import requests

# Step 1: Get the login page
response = requests.get('https://texastech.rivals.com/users/sign_in')
cookies = response.cookies
# You may need to parse the response content to find hidden form fields

# Step 2: Prepare the login data
login_data = {
    'login': 'your_username',
    'password': 'your_password',
    # Add any other required fields here
}

# Step 3: Post the login request
login_response = requests.post('https://texastech.rivals.com/users/sign_in', data=login_data, cookies=cookies)

# Step 4: Check if login was successful
if login_response.ok:
    print('Logged in successfully!')
else:
    print('Failed to log in.')


######################

# I think this works

from scrapingbee import ScrapingBeeClient
import os

MAIN_URL = "https://n.rivals.com/users/sign_in"

scraping_bee_key = os.environ.get("scraping_bee_key")
client = ScrapingBeeClient(api_key=scraping_bee_key)

response = client.post( # Using a POST request instead of GET
    MAIN_URL,
    data= { # Data to send with our POST request
        "login": "CJK5Hookers", # Login email
        "password": "cjk5hcjk5hc" # Login password
    }
)

if response.ok:
    with open("screenshot.html", "wb") as f:
        f.write(response.content)
else:
    print(response.content)


##############

from scrapingbee import ScrapingBeeClient

MAIN_URL = "https://texastech.forums.rivals.com/threads/texas-tech-v-kansas-pres-by-js-salsa-ttu-wins-16-13.185484/"

client = ScrapingBeeClient(api_key='2ZWMVWN5PU27Q17JPT253FH9GZIGX4A5YJ4FCUFIU7KNTM1Y21MJ4YVKXLQE87O6YJMSRP1W61VBMIGP')
response = client.get(
    MAIN_URL,
    cookies = {"PrestaShop-a30a9934ef476d11b6cc3c983616e364": "Cookie-Text-Here"},
    params= {
        "screenshot_full_page": True,
    }
)
if response.ok:
    with open("./screenshot.png", "wb") as f:
        f.write(response.content)
else:
    print(response.content)
    
    
###################
    
import requests
from bs4 import BeautifulSoup

# Step 1: Create a session object
session = requests.Session()

# Step 2: GET request to retrieve the XSRF token
response = session.get("https://n.rivals.com/users/sign_in")
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Parse the XSRF token from the HTML (or cookie)
# This assumes the token is in a hidden form field named 'xsrf_token'
xsrf_token = soup.find('input', attrs={'name': 'xsrf_token'})['value']
