from bs4 import BeautifulSoup as sp
from urllib.request import urlopen
from urllib.parse import urlparse
import requests, bs4
import time
import csv
import os
from selenium import webdriver
url="https://www.youtube.com/results?search_query="

def scrollDown(pause):
    """
    Function to scroll down till end of page.
    """
    lastHeight = webdriver.execute_script("return document.body.scrollHeight")

    while True:
        webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        newHeight = webdriver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight

with open("youtubedata.csv", 'w',encoding="utf-8") as f:
    cw = csv.writer(f)
    fields = ["VideoID", "Title" ,"Description" ,"Class"]
    cw.writerow(fields)

category = ["Art and Music","Food","Manufaturing","History","Science and Technology","Travel Blogs"]
for topic in category:
    full_url = url+topic.replace(" ","+")
    
    driver=webdriver.Chrome(r"C:/Users/Vidyajay/Desktop/Harshit/chromedriver.exe")
    driver.get(full_url)
    driver.execute_script('window.scrollTo(1, 500);')
    #now wait let load the videos
    for i in range(50):
        driver.execute_script("window.scrollTo(0, 3600*"+str(i)+');')
        time.sleep(1)
        count=0

    page_html = driver.page_source
    soup = sp(page_html,"html.parser")
    #print(soup.prettify())
    #print()
    
    description = soup.find_all("h3",{"class":"title-and-badge" }) 
    print(description)

    
    with open("youtubedata.csv", 'a', encoding="utf-8") as f:
        cw = csv.writer(f)
        for i in range(0,len(description)):
            title = description[i].a["title"]
            print(title)
            link = description[i].a["href"]
            if "googleadservices" in link:
                continue
            desc_url = "https://www.youtube.com" + link
            try:
                video_id = desc_url.split('=')[1]
            except IndexError:
                continue
            print(desc_url)
            print(video_id)
            
            req = requests.get(desc_url)
            info = req.text
            soup1 = sp(info,"html5lib")
            container = soup1.find("p",{"id":"eow-description"})
            #print(container)
            body=str(container)
            
            data = [video_id, title, body, topic]
            cw.writerow(data)
f.close()