
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\Dhruv Bajaj\Downloads\webdriver\chromedriver.exe")
import pandas as pd
import time
import os

driver.get("https://www.angloinfo.com/kuala-lumpur/directory/kuala-lumpur-osteopaths-chiropractors-physiotherapists-552")

driver.minimize_window()

#storeDetails = driver.find_elements_by_class_name('media listing list-free')
names = driver.find_elements_by_class_name('item-name')
contactList = driver.find_elements_by_class_name('hidden-phone')

nameList = []
#addressList = []
numbersList = []

for i in range(len(names)):

    name = names[i].text
    #address = storeDetails[i].text
    #contact = contactList[i].get_attribute("innerHTML")
    contact = contactList[i].text
    nameList.append(name)
    #addressList.append(address)
    numbersList.append(contact)


# data lists.
data = {'Doctors':nameList,
        #'Address': addressList,
        'Phone':numbersList
        }

# Create DataFrame using pandas
df = pd.DataFrame(data)
print(df)

# Save Data as .csv
df.to_csv('demos4.csv', mode='a', header=False)


print("finished")