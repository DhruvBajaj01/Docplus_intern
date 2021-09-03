
from selenium import webdriver
import pandas as pd
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome(executable_path=r"C:\Users\Dhruv Bajaj\Downloads\webdriver\chromedriver.exe")
driver =webdriver.Chrome(executable_path=r"C:\Users\Dhruv Bajaj\Downloads\webdriver\chromedriver.exe")

def urls():
    df_main=pd.DataFrame()
    doc_name_list=[]
    doc_tel_list=[]
    doc_loc_list=[]
    doc_email_list=[]
    for i in range(20):
        #Get list of doctor names
        name_list = driver.find_elements_by_tag_name("name")#Get all the card list
        n_lt=driver.find_elements_by_tag_name("url")#Get list of doctor names
        name_list[i].find_element_by_link_text(n_lt[i].text).click()
        try:

            name=driver.find_element_by_tag_name('name').text
        except:
            name=driver.find_element_by_tag_name('name').text

        doc_name_list.append(name)



        try:

            tel1=driver.find_element_by_tag_name("telephone").text
        except:
            tel1=''

        doc_tel_list.append(tel1)
        try:

            loc_ele=driver.find_element_by_id("location")
        except:
            loc_ele=None
        try:
            loc=loc_ele.find_element_by_tag_name("streetAddress").text
        except:
            if(loc_ele==None):
                loc=None
            else:
                loc=loc_ele.text
        doc_loc_list.append(loc)
        try:
            email=driver.find_element_by_tag_name("paymentAccepted").text
        except:
            email="None"
        doc_email_list.append(email)


        driver.back()
    return pd.DataFrame({'name':doc_name_list ,'pay': doc_email_list ,'location': doc_loc_list,'telephone': doc_tel_list})
driver.get("https://www.medicineindia.org/pharmacies-chemists-drugstores-in-city/190/chandigarh")
df_doc=urls()
df_main_doc=df_doc.append(df_doc)
df = pd.DataFrame(df_main_doc)
print(df)

# Save Data as .csv
df.to_csv('file.csv', mode='a', header=False)


