import sqlite3


print("Configuring Sqlite db.")
conn = sqlite3.connect('twitch.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE chat_messages (user text, message text)''')

# Insert a row of data
c.execute("INSERT INTO chat_messages VALUES ('2006-01-05','BUY')")

# Save (commit) the changes
conn.commit()
conn.close()