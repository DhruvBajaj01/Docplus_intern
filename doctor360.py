from bs4 import BeautifulSoup
import requests
area = (str(input()))
category = (str(input()))
source = requests.get(f'https://www.doctor360.in/{area}/{category}').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('div', class_='listing-item text-left'):

    name = article.find('div', class_='col-md-12 col-xs-12 col-sm-12 title').h2.text
    print("Name",name)
    specialist = article.find('div', class_='col-md-12 col-xs-12 col-sm-12 title').h3.text
    print("Speciality",specialist)
    Details = article.find('div', class_='col-md-5 col-sm-4 col-xs-6 info1').text
    print("Details :",Details)
    print()



  
   