import sqlite3
conn = sqlite3.connect('dublinbikes.sqlite')
c = conn.cursor()
c.execute('''SELECT * FROM dublinbikes ''')
count = 1
for row in c:
		print(row)