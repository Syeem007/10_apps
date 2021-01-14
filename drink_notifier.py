import time
from plyer import notification
import sys

if __name__ == '__main__':
    while True:
        notification.notify(
            title='**Please drink water**',
            message='Drink water',
            app_icon=(sys.path.append(r'C:\Users\Syeem\PycharmProjects\10projects_1-10\img.png')),
            timeout='10'
        )
        time.sleep(60 * 60)
