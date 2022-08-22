print("Wel come to the new channel")
import requests
import bs4
# url="https://www.mohfw.gov.in/"
# url="https://covid19.mohp.gov.np/#/"
url="https://www.hamropatro.com/"
data=requests.get(url)
print(data.text)
files="Panta.html"
ob=bs4.BeautifulSoup(data.text,"html.parser")
style=ob.prettify()
# print(style)
data=ob.find("div",class_="horizontal-scroll").find('div',class_="covid-conntainer item").find('div',class_="header-covid")
for block in data:
    print(block)
# print(data)
 
