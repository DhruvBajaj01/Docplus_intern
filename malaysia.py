
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\Dhruv Bajaj\Downloads\webdriver\chromedriver.exe")
import pandas as pd
import time
import os

driver.get("https://www.angloinfo.com/kuala-lumpur/directory/kuala-lumpur-paediatricians-627")

driver.minimize_window()


names = driver.find_elements_by_class_name('item-name')

con= driver.find_elements_by_class_name('show-number')


nameList = []

addressList = []
contactList =[]

for i in range(len(names)):

    name = names[i].text

    contact = con[i].get_attribute("innerHTML")

    address = "kuala Lumpur"
    nameList.append(name)

    addressList.append(address)
    contactList.append(contact)

# data lists.
data = {'Doctors':nameList,
        'contact':contactList,
        'address': addressList
        }

# Create DataFrame using pandas
df = pd.DataFrame(data)
print(df)

# Save Data as .csv
#df.to_csv('demo.csv', mode='a', header=False)


print("finished")