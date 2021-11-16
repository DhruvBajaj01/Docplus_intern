import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import numpy as np
from bs4 import BeautifulSoup
import time, os, requests, csv

options = webdriver.ChromeOptions()
# options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

prefs = {"profile.default_content_setting_values.notifications": 2}

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def second(l):
    source = requests.get(l).content
    soup = BeautifulSoup(source, 'lxml')
    #print(source)
    name = soup.find('div', class_='info col-md-9 col-sm-12 col-lg-9').h1.text
    # print("Name :",name)
    specialist = soup.find('div', class_='info col-md-9 col-sm-12 col-lg-9').find("h2", class_="head-address text-capitalize").text
    # print("Speciality :",specialist)
    rating = soup.find("div", class_='rating-number').text
    # print("Rating :",rating)
    Address = soup.find('div', class_='col-md-5 col-lg-5 col-sm-12').find('div').find("span", class_="info_data").text
    # print("Address :",Address)
    Details = soup.find('div', class_='col-md-5 col-lg-5 col-sm-12').find('div').find("h2", class_="info_data").text
    # print("Clinic :",Details)
    Details_1 = soup.find('div', class_='col-md-7 col-lg-7 col-sm-12 extra_info table-responsive').text
    # print("Other Details :",Details_1)
    Treatment = soup.find_all("ul",class_="condition-list")[0].find_all("li", class_="service-list-item")
    lst=[]
    for i in Treatment:
        lst.append(i.text)
    # print("Procedure :",lst)
    conditionsTreated = soup.find_all("ul",class_="condition-list")[2].find_all("li", class_="service-list-item")
    lst1=[]
    for i in conditionsTreated:
        lst1.append(i.text)
    # print("Conditions Treated :",lst1)

    d= {
        'doctor_name': name,
        'Rating':rating,
        'Speciality': specialist,
        'Address': Address ,
        'Clinic': Details,
        'Other Details': Details_1,
        'Procedure': lst,
        'Conditions Treated': lst1
    }



    return d


def btnClick(path):
    conButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, path)))
    conButton.click()

# called to send input
def sendInput(path, data):
    location = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, path)))
    location.clear()
    location.send_keys(data)
    time.sleep(3)


def info(city,doc):

    url="https://www.doctor360.in/"
    driver.get(url)
    time.sleep(2)
    # btnClick('//*[@id="react-select-location_select-input"]')
    sendInput('//*[@id="react-select-location_select-input"]', city)

    # item = driver.find_element_by_class_name('css-kj6f9i-menu')
    # print(item.text)
    btnClick('//*[@id="react-select-location_select-option-0"]/div/i')
    time.sleep(3)

    # btnClick('//*[@id="react-select-value_select-input"]')
    sendInput('//*[@id="react-select-value_select-input"]', doc)

    # soup = BeautifulSoup(driver.page_source, 'lxml')
    # with open('sample_2.html', 'w') as file:
    #     file.write(soup.prettify())
    time.sleep(3)
    doc_profile_url = driver.find_element(By.XPATH, '//*[@id="react-select-value_select-option-0"]/a').get_attribute('href')
    print('\n\n',doc_profile_url)
    he = second(doc_profile_url)
    return he


l=info("Delhi","Dr. Gorav Gupta")
print(l)
# print([[key,value] for key,value in l])
driver.close()






