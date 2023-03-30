import time, json
from selenium import webdriver
from selenium.webdriver.common.by import By


MAX_HISTORY_SIZE = 150
OUTPUT_JSON_FILE = "history.json"
TWITCH_CHANNEL = "marex"

# options = webdriver.FirefoxOptions()
# options.add_argument('-headless')

browser = webdriver.Firefox()
browser.get(f'https://www.twitch.tv/{TWITCH_CHANNEL}')

last_message = ''
history = {}

try:
    i = 0
    while True:
        chat_messages = browser.find_elements(By.CLASS_NAME,'chat-line__message')

        for message in chat_messages:
            str_message = str(message.text)
            user, m = str_message.split(':', maxsplit=1)
            
            if history.get(user) is None:
                history[user] = []

            # Check if the message is already in the user's history
            if m[1:] in history[user]:
                pass
            else:
                history[user].append(m[1:])
                if not m:
                    emotes = message.find_elements(By.CLASS_NAME,'chat-line__message--emote')
                    emotes_messages = ' '.join([em.get_attribute('alt') for em in emotes])
                    print("{}: {}".format(user, emotes_messages))
                    continue
                
                print("{}: {}".format(user, m[1:]))

        time.sleep(5)
        i += 1
        if i == MAX_HISTORY_SIZE:
            print("\n*2", "==== Saved to file ====", "\n*2")

            # Save history to a JSON file
            with open(OUTPUT_JSON_FILE, 'a') as f:
                f.write(json.dumps(history))
                f.write(',\n')
            history.clear()
            i = 0

except Exception:
    browser.quit()
    raise Exception
