from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from plyer import notification
import time
from win10toast import ToastNotifier

header = {'User-agent': 'Google Chrome'}
req = Request('https://www.worldometers.info/coronavirus/country/bangladesh/', headers=header)
html = urlopen(req)
obj = bs(html)
var = obj.find('li', {'class': 'news_li'}).strong.text.split()[0]
var1 = list(obj.find('li', {'class': 'news_li'}).strong.next_siblings)[1].text.split()[0]

while True:
    notification.notify(
        title='covid notification',
        message=var + '\nDeath' + var1,
        # app_icon=(sys.path.append(r'C:\Users\Syeem\PycharmProjects\10projects_1-10\img.png')),
        timeout='50'
    )
    time.sleep(1 * 60)
