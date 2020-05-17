import sqlite3


conn = sqlite3.connect('twitch.db')
c = conn.cursor()

for row in c.execute("SELECT * FROM chat_messages;"):
    print(row)

conn.close()