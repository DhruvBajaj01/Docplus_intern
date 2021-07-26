
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
        name_list = driver.find_elements_by_class_name("idBusinessCardType")#Get all the card list
        n_lt=driver.find_elements_by_class_name("nameOverflow")#Get list of doctor names
        name_list[i].find_element_by_link_text(n_lt[i].text).click()
        try:

            name=driver.find_element_by_class_name('yext-name').text
        except:
            name=driver.find_element_by_tag_name('h2').text

        doc_name_list.append(name)

        b_list=driver.find_elements_by_tag_name("b")
        for j in range(4):
            b_list[j].click()
        try:

            tel1=driver.find_element_by_class_name("yext-phone").text
        except:
            tel1=''
        try:
            tel2=driver.find_element_by_class_name("yext-alt").text
        except:
            tel2=''
        doc_tel_list.append(tel1+'|'+tel2)
        try:

            loc_ele=driver.find_element_by_id("location")
        except:
            loc_ele=None
        try:
            loc=loc_ele.find_element_by_tag_name("a").text
        except:
            if(loc_ele==None):
                loc=None
            else:
                loc=loc_ele.text
        doc_loc_list.append(loc)
        try:
            email=driver.find_element_by_class_name("yext-emails").text
        except:
            email="None"
        doc_email_list.append(email)


        driver.back()
    return pd.DataFrame({'name':doc_name_list ,'email': doc_email_list ,'location': doc_loc_list,'telephone': doc_tel_list})
driver.get("https://www.yellowpages.co.za/search?what=doctors&pg=10")
df_doc=urls()
df_main_doc=df_doc.append(df_doc)
df = pd.DataFrame(df_main_doc)
print(df)

# Save Data as .csv
df.to_csv('file.csv', mode='a', header=False)


