import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


URL = 'https://www.airvistara.com/gst/login'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
df = pd.read_excel(r'C:\Users\Sguha\Downloads\GST_UPLOAD_TEMPLATE.xlsx')
def vistara_ticket_status(username,password):
    url = f"https://www.airvistara.com/gst/login/"
    response = requests.get(url)
    if response.status_code == 200:
        driver = webdriver.Chrome()
        driver.get("https://www.airvistara.com/gst/login")
        username = driver.find_element_by_id('username')
        password = driver.find_element_by_id('password')
        username.send_keys('your_username')
        password.send_keys('your_password')
        text_box = driver.find_element_by_id('text-box')
        for data in df['TICKET_NUMBER','PNR','DATE_OF_ISSUANCE']:
            text_box.send_keys(data)
            driver.find_element_by_id('Next').click()
            driver.find_element_by_id('Next').click()
            driver.find_element_by_id('No Thanks, Download Later').click()
            driver.find_element_by_id('Profile').click()
            driver.find_element_by_id('My Transactions').click()
            driver.find_element_by_id('Download Invoice').click()
            driver.quit()
        df['Download Status'] = 'Valid'
    else:
        df['Download Status'] = 'Invalid'
df.to_csv(r'C:\Users\Sguha\Downloads\GST_UPLOAD_TEMPLATE.csv')

