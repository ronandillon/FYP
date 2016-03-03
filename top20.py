import json
import urllib2
import sqlite3

conn = sqlite3.connect('testytest.db')
c = conn.cursor()
query =c.execute("SELECT * FROM Show ORDER BY count DESC LIMIT 20")
returns =query.fetchall()

print returns[1][2]
