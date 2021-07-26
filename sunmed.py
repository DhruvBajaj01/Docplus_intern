from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver")
import pandas as pd
doc_name_list = []
doc_tel_list = []
doc_loc_list = []
doc_spec_list = []
doc_hospital=[]
url="https://www.sunwaymedical.com/find-a-doctor/search/200/?specialty=&doctor=&name="

driver.get(url)
name=driver.find_elements_by_class_name("doctor_name")
for n in name:
    doc_name_list.append(n.text)
    doc_hospital.append("Sunway Medical Centre")
for i in range(2,42,2):
    doc_tel_list.append("+603-7491 9191")

    try:
        doc_loc_list.append(driver.find_element_by_xpath("//*[@id='content']/div/div/div/div[1]/div[1]/div["+str(i)+"]/div[2]/div[19]").text)
    except:
        doc_loc_list.append('None')
    doc_spec_list.append(driver.find_element_by_xpath("//*[@id='content']/div/div/div/div[1]/div[1]/div["+str(i)+"]/div[2]/div[23]").text)

append_str = '-Bandar Sunway, 47500 Selangor, Malaysia.'

# Append suffix / prefix to strings in list
pre_res = [append_str + sub for sub in doc_loc_list]
suf_res = [sub + append_str for sub in doc_loc_list]
print(len(doc_loc_list))
print(len(suf_res))
data={'name': doc_name_list,'location': suf_res, 'telephone': doc_tel_list,'Specialiy':doc_spec_list,'Hospital':doc_hospital}
df = pd.DataFrame(data)
print(df)

# Save Data as .csv
df.to_csv('malaysia10.csv', mode='a', header=False)