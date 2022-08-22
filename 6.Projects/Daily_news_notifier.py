'''
pip install feedparser
'''
import feedparser
from plyer import notification
import time
def parseFeed():
    f=feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")
    # print(f)
    for newsitem in f['items']:
        notification.notify(title=newsitem['title'],
        message=str(newsitem['summary']),timeout=100)
        time.sleep(60)
if __name__ == '__main__':
    parseFeed()
            