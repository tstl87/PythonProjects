# -*- coding: utf-8 -*-
"""
The purpose of this program is to prevent windows users
from accessing some websites during certain times of the day.
"""
import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    
    if dt( dt.now().year, dt.now().month, dt.now().day, 9 ) < dt.now() < dt( dt.now().year, dt.now().month, dt.now().day, 17 ):
        
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            # record content of hosts file
            content = file.read()
            # add websites to block if they aren't already on the list
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            # record each line of hosts file
            # as an element of a list
            content = file.readlines()
            # bring pointer back to the start of the document
            file.seek(0)
            # look for lines that do not contain any of the blocked websites
            # and write them back into hosts file
            for line in content:
                if not any( website in line for website in website_list):
                    file.write(line)
            # delete all lines that follow.
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
    