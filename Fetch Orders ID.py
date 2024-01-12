
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import glob



### Initialisation ####

cookies = { "I can't show them here, but they are found in the console mode of your browser when visiting the website in question, under the headers settings." }

headers = { "I can't show them here, but they are found in the console mode of your browser when visiting the website in question, under the headers settings."}

data = {
    '_token': '',
    'remember': '1',
    'email': 'email',
    'password': 'password',
}

#### Session pour aller chercher l'information ####

with requests.Session() as s:
    # --- first GET page ---

    response = s.get(url='The URL of the website I used for my orders', headers=headers)

    # --- search fresh token in HTML ---

    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find('input', {'name': "_token"})['value']

    # --- run POST with new token ---

    data['_token'] = token

    response1 = s.post('https://brickfreedom.com/login', cookies=cookies, headers=headers, data=data)
    soup = BeautifulSoup(response1.content, "html.parser")

    # --- loading order pages --- #

    response = s.get('The URL of the website I used for my orders', cookies=cookies, headers=headers, data=data)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all(name = "div", attrs={'class:', 'mt-1 absolute flex items-center h-5'})

    #### Créer le dictionnaire avec les deux ID ####

    d = {"ID_BF":[], "ID_BLBO":[]}
    for i in results:
        d['ID_BF'].append(i.find('input')['value'])
    liste_ID = []

    IDs = soup.find_all(name="div", attrs = {'class': ['flex items-center text-sm leading-5 font-medium']})
    for i in IDs:
        i_formater = [text for text in i.stripped_strings][1]
        d["ID_BLBO"].append(i_formater)


#### Selenium session ####

options = Options()
prefs = {"download.default_directory": "Your\\Path"}
options.add_experimental_option("prefs", value = prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


driver.get('The Website I used for my orders')

email = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")

email.send_keys("email")
password.send_keys("password")
driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div/button').click()


#### Créer un CSV contenant l'url des IDs Brickfreedom ####

os.remove("K:\\My Drive\\Automatisation\\b.csv")

i = 0
url_orders = "The URL of the website I used for my orders"
header = ['ID_BF', 'ID_BLBO']
with open('b.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for value in d['ID_BF']:
        row = [d['ID_BF'][i], d['ID_BLBO'][i]]
        writer.writerow(row)
        i += 1
i = 0
for value in d['ID_BF']:
    url_orders = url_orders + d['ID_BF'][i] + ","
    i += 1


driver.get(url_orders)

driver.find_element_by_xpath('/html/body/div/div[3]/main/div[2]/div/div[1]/div/form[2]/div/div/button').click()
time.sleep(3)

os.remove("Your\\Path")
home = os.path.expanduser('~')
path = os.path.join(home, 'Your\\Path')

path_a = path + "/*.csv" # * means (match all), if specific format required then *.csv This will get all the files ending with .csv
list_of_files = glob.glob(path_a)
latest_file = max(list_of_files, key=os.path.getctime)

new_file = os.path.join(path, "filename.csv")
os.rename(latest_file, new_file)
driver.quit()













