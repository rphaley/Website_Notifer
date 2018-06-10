from lxml import etree, html
from sendEmail import sendEmail
import requests, time, random, datetime

timeLow = 180
timeHigh = 480

while True:
    page = requests.get('https://www.blackhat.com/us-18/training/index.html')
    d = etree.HTML(page.text)
    status = d.xpath('//*[@id="adversary-tactics-red-team-ops"]/div[1]/div[2]/@class')
    if "course-sold-out-graphic" not in status:
        CN = "Train"
        msg = 'https://www.blackhat.com/us-18/training/adversary-tactics-red-team-ops.html'
        sendEmail("Blackhat training now available!",msg,CN)
    else:
        tStamp = datetime.datetime.now()
        print('[{:%H:%M %m/%d/%y}]Status unchanged. Sleeping...'.format(tStamp))
    time.sleep(random.randint(timeLow,timeHigh))
