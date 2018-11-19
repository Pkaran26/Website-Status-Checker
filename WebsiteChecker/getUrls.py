#!C:\Users\Anchal\AppData\Local\Programs\Python\Python37-32\python.exe

import mysql.connector
import json
print ("Content-type:application/json\n")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="websites"
)

cur = mydb.cursor()
cur.execute("select url from urls")
res = cur.fetchall()
print(json.dumps(res))