from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\Dhruv Bajaj\Downloads\webdriver\chromedriver.exe")
import pandas as pd
import time
import os

driver.get("https://www.primarycarepages.sg/useful-links/locate-a-service-near-you/find-a-doctor")

driver.minimize_window()

#storeDetails = driver.find_elements_by_class_name('media listing list-free')
names = driver.find_elements_by_class_name('accordion')
exp = driver.find_elements_by_tag_name('ctl00_ctl50_g_e1204710_5ea4_4047_b706_3f65088d78f5_rptClinicResults_ctl01_lblPhone')
spL = driver.find_elements_by_tag_name('ctl00_ctl50_g_e1204710_5ea4_4047_b706_3f65088d78f5_rptClinicResults_ctl01_lblAddress')

nameList = []
#experienceL = []

#spList = []
#degreeL = []

for i in range(len(names)):
    #Deg = degree[i].text
    name = names[i].text

    #e=exp[i].getAttribute
    # contact = contactList[i].get_attribute("innerHTML")
    #sp = spL[i].text



    nameList.append(name)
    #experienceL.append(e)
    #addressList.append(address)
    #spList.append(sp)
    #degreeL.append(Deg)

# data lists.
data = {'Doctors':nameList,
        #'Experience':experienceL,

        #'Address': addressList,
        #'Specialization':spList,
        }

# Create DataFrame using pandas
df = pd.DataFrame(data)
print(df)

# Save Data as .csv
#df.to_csv('demo.csv', mode='a', header=False)


print("finished")