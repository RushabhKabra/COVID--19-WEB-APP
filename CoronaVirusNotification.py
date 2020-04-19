from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="icon.ico",
        timeout=24
    )

def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        # notifyMe("Rushabh","lets get this virus out together")
        myHtmlData=getData("https://www.mohfw.gov.in/")

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr=""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr+=tr.get_text()
        myDataStr=myDataStr[1:]
        itemList=myDataStr.split("\n\n")

        states=['Gujarat','Rajasthan','Maharashtra']
        for item in itemList[0:23]:
            dataList=item.split("\n")
            if dataList[1] in states:
                print(dataList)
                nTitle='Cases of COVID-19'
                nText=f"STATE : {dataList[1]}\nIndian : {dataList[2]} Foreign : {dataList[3]}\nCured/Discharged/Migrated : {dataList[4]}\nDeath : {dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(2)
        #time.sleep(3690)        
