
import requests 
from bs4 import BeautifulSoup

URL = "https://fc2.com/en//"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib')
tag1= soup.find_all('div', attrs ={"class":"content_body"}) 
for tag2 in tag1:
    tag3=tag2.find_all('div',attrs={"class":"service_body"})
    print(tag3.div.dl.dd.text)