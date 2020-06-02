from sendEmail import sendEmail
import requests, time, datetime, os

#Time in between checks
sleepTime = 2
#Number of failures before alert is generated
cnt = 0

logName = "WebLog"
host = 'website1'
error = 'website down'
reason = 'unreachable'

while True:
        if cnt == 3:
                CN = "host1"
                msg = 'Website not responding'
                title = "Website not responding"
                sendEmail(title,msg,CN)
                with open('{}-{:%m_%d}.log'.format(logName,datetime.datetime.now()), 'a') as f:
                        f.write('{:%Y-%m-%d %H:%M:%S},{},Website down, email sent.\n'.format(datetime.datetime.now(),host))
        try:
                requests.get('http://c2.depaulseclabs.com', timeout=2, verify=False)
                print('[{:%H:%M %m/%d/%y}]Status unchanged. Sleeping...'.format(datetime.datetime.now()))
        except Exception as e:
                cnt += 1
                with open('{}-{:%m_%d}.log'.format(logName,datetime.datetime.now()), 'a') as f:
                        f.write('{:%Y-%m-%d %H:%M:%S},{},{},{}\n'.format(datetime.datetime.now(),host,error,reason))
        finally:
                time.sleep(sleepTime)


