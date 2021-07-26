# importing the modules
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=r"C:\Users\Dhruv Bajaj\Downloads\webdriver\chromedriver.exe")
import pandas as pd
import time
import os

# driver.get method() will navigate to a page given by the URL address
for i in range(1,51):

    driver = webdriver.Chrome(executable_path=r"C:\Users\Dhruv Bajaj\Downloads\webdriver\chromedriver.exe")
    #driver.get("https://www.justdial.com/Kanpur/General-Physician-Doctors/nct-10892680")
    url="https://www.justdial.com/Kanpur/General-Physician-Doctors/nct-10892680/page-{}".format(i)
    driver.get(url)
    i=i+1
    print("page {}".format(i))
    driver.minimize_window()


    # The given function is to decode the phone no from the website
    def strings_to_num(argument):

        switcher = {
            'dc': '+',
            'fe': '(',
            'hg': ')',
            'ba': '-',
            'acb': '0',
            'yz': '1',
            'wx': '2',
            'vu': '3',
            'ts': '4',
            'rq': '5',
            'po': '6',
            'nm': '7',
            'lk': '8',
            'ji': '9'
        }
        return switcher.get(argument, "nothing")
    # details of the store
    Details = driver.find_elements_by_class_name('store-details')

    nameList = []
    addressList = []
    numbersList = []
    # getting details
    for i in range(len(Details)):

        name = Details[i].find_element_by_class_name('lng_cont_name').text # adds name of doctors from main webpage
        address = Details[i].find_element_by_class_name('cont_sw_addr').text # adds address of clinic
        contact = Details[i].find_elements_by_class_name('mobilesv') # get information of mobile no on webpage

        myList = []

        for j in range(len(contact)):

            myString = contact[j].get_attribute('class').split("-")[1]

            myList.append(strings_to_num(myString)) # use to convert the cipher text into number by using th function

        nameList.append(name)
        addressList.append(address)
        numbersList.append("".join(myList))


    # data lists.
    data = {'Doctors':nameList,
            'Address': addressList,
            'Phone':numbersList}

    # Create DataFrame using pandas
    df = pd.DataFrame(data)
    print(df)

    # Save Data as .csv
    df.to_csv('Kanpur_Doctors.csv', mode='a', header=False)


print("code finished")