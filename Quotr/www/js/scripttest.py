#!/usr/python
import cgi
print('Content-Type: text/html; charset=utf-8\n')
form = cgi.FieldStorage()

form={name:"Ro"};
with open('/var/www/cgi-bin/temp.txt','w') as file:
    file.write(form['name'])
