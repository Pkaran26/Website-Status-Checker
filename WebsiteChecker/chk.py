#!C:\Users\Anchal\AppData\Local\Programs\Python\Python37-32\python.exe
import requests
import cgi
print ("Content-type:text/html\n")

def chkUrl(url):
    try:
        data = requests.get(url)
        return data.status_code
    except:
        #requests.exceptions.ConnectionError as err
        return '404'

param = cgi.FieldStorage()
print(chkUrl(param['url'].value))