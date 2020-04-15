import requests
from bs4 import BeautifulSoup
url=input("BULMAK ISTEDIGINIZ SAYFANIN URLSINI GIRINIZ ==>")
tag=input("SAYFADA ARADIGINIZ TAG(a,script,class)")
clas=input("BULMAK İSTEDİĞİNİZ CLASS")
response=requests.get(url)
icerik=response.content
soup=BeautifulSoup(icerik,"html.parser")
script=soup.find_all(tag,{"class":clas})
for i in script:
    print(i.text)
    print("-------")