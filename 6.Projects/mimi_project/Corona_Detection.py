print("Starting")
import requests
import bs4
def get_html_data(url):
    data=requests.get(url)
    return data
def get_corona_detail():
    # url="https://covid19.mohp.gov.np/#/"
    url="https://www.mohfw.gov.in/"
    # url="https://www.booking.com/index.en.html?aid=309654;label=hotels-english-en-row-bu5VMQshEg4nFfJmgdu6ZwS228854886432:pl:ta:p1:p22,563,000:ac:ap:neg:fi:tikwd-185941336:lp9070016:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YcsZ-Id2vkzIfTmYhvC5HOg;ws=&gclid=CjwKCAjwjLD4BRAiEiwAg5NBFnaN9t_OhUuRt8FnMw7xvaqhSSDUQMmiPfEcd5TggEP1UJm_IMezxxoCDpcQAvD_BwE"
    html_data=get_html_data(url)
    # print(html_data.text)
    bs=bs4.BeautifulSoup(html_data.text,'html.parser')
    # print(bs.prettify())
    info_div=bs.find("section",class_="site-stats").find_all("li",class_="site-stats-count")
    # info_div=bs.find("ul",class_="site-stats-count")
    # print(info_div)
    # print(len(info_div))
    for block in info_div:
        print(block) 
        text=block.find("strong",class_="bg-blue").get_text()
        count=block.find("span",class_="bg-blue").get_text()
        print(text+":"+count)
        # print(count)
    
       

    print("Thanks")



get_corona_detail()        