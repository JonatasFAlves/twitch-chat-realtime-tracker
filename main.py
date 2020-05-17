import time
import sqlite3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
options.add_argument('-headless')

browser = webdriver.Firefox(executable_path='/usr/bin/geckodriver', firefox_options=options)
browser.get('https://www.twitch.tv/albralelie')


last_message = ''

try:
    while True:
        chat_messages = browser.find_elements_by_class_name('chat-line__message')

        for message in chat_messages:
            str_message = str(message.text)
            user, m = str_message.split(':', maxsplit=1)
            
            if not m:
                emotes = message.find_elements_by_class_name('chat-line__message--emote')
                emotes_messages = ' '.join([em.get_attribute('alt') for em in emotes])
                print("{}: {}".format(user, emotes_messages))

                continue


            print("{}: {}".format(user, m[1:]))

        time.sleep(5)
except Exception:
    browser.quit()
    raise Exception