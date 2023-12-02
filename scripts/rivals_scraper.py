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
# chromedriver_autoinstaller.install()
from bs4 import BeautifulSoup
import csv

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

driver =webdriver.Chrome(options=get_new_options())
driver.maximize_window()
driver.get('https://n.rivals.com/users/sign_in')
sleep(2)
driver.find_element(By.XPATH,'//input[@name="login"]').send_keys('EB1TDA')
sleep(1)
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('heaven123')
sleep(1)
driver.find_element(By.XPATH,'//button[@class="Button_button___KSka Button_medium__N5gPS"]').click()
sleep(10)
# base_page_link = 'https://texastech.forums.rivals.com/threads/texas-tech-v-texas-ut-57-7-4q-pres-by-js-salsa.186034/page-'
base_page_link = 'https://texastech.forums.rivals.com/threads/texas-tech-v-central-florida-ttu-24-23-4q-pres-by-js-salsa.185779/page-'

# update this for final
number_of_pages = 43
post_list = []

for n in range(0, number_of_pages):
    target_url = str(base_page_link + str(n+1))
    print('Navigating to page: ' + target_url)
    driver.get(target_url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    # Find all instances of <div class="message-inner">
    message_inner_elements = soup.find_all('div', class_='message-inner')
    # Iterate through each <div class="message-inner">
    for message_inner in message_inner_elements:
        message_data = {}
        # Extract text from the time class with data-time-string attribute
        time_element = message_inner.find('time', class_='u-dt')
        if time_element:
            data_time_string = time_element['data-time-string']
            print("Text from data-time-string in the time class:", data_time_string)
            message_data['time_element'] = data_time_string
        else:
            message_data['time_element'] = ""
        # Extract text from itemprop="name"
        name_element = message_inner.find('span', itemprop='name')
        if name_element:
            name_text = name_element.text
            print("Text from itemprop='name':", name_text)
            message_data['username'] = name_text
        else:
            message_data['username'] = ""
        # Extract text from <div class="bbWrapper">
        bb_wrapper_element = message_inner.find('div', class_='bbWrapper')
        if bb_wrapper_element:
            # remove escape characters
            bb_wrapper_text = bb_wrapper_element.text.replace('\n', ' ').replace('\t', ' ')
            print("Text from <div class='bbWrapper'>:", bb_wrapper_text)
            message_data['post_text'] = bb_wrapper_text
        else:
            message_data['post_text'] = ""
        message_data['thread_page'] =  str(n+1)
        # Add a separator between each <div class="message-inner">
        print("-" * 50)
        # only add to post list if all items aren't blank, this ensure you don't get any non-post html
        if message_data['time_element'] and message_data['username'] and message_data['post_text']:
            post_list.append(message_data)
