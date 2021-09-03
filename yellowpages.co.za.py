import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

import time
import os

#create list of urls to traverse
url=[]
for i in range(1,301):
    s1="https://www.yellowpages.co.za/search?what=doctors&pg="
    s2=str(i)
    s=s1+s2
    url.append(s)

#create function for Dataset
def urls():
    
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

#traversing all urls and running function
df_main=pd.DataFrame()
for i in range(len(url)):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url[i])
    df_doc = urls()
    df_main_doc=df_main_doc.append(df_doc)
    driver.quit()