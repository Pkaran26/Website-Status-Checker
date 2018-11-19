#!C:\Users\Anchal\AppData\Local\Programs\Python\Python37-32\python.exe
import urllib.request
import cgi
print ("Content-type:text/html\n")

def chkUrl(url):
    url.strip()
    try:
        return urllib.request.urlopen(url).getcode()
    except:
        return '404'

param = cgi.FieldStorage()
print(chkUrl(param['url'].value))