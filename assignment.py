#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:00:43 2019

@author: manzars
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time

req = webdriver.Firefox()
url = 'https://www.vdma.org/en/mitglieder?p_p_lifecycle=2&p_p_resource_id=getPage&p_p_id=vdma2publicusers_WAR_vdma2publicusers&s=&page='
req.get(url)
file = open('assignment.csv', 'w')
header = 'Company Name, Email, Telephone, Website, Address\n'
file.write(header)
for i in range(1, 330):
    time.sleep(1)
    req.get(url + str(i))

    
    html = req.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.findAll('div', {'class': 'vdma-public-member'})

    for element in elements:
        name, website, addr, tele, email, telep = '', '', '', [], '', ''
        name = element.findAll('div', {'class': 'col-xs-7 col-sm-7 col-md-7 col-lg-7 text-left'})
        name = name[0].contents[1].text
        #print(name)
        
        website = element.findAll('div', {'class': 'col-xs-5 col-sm-5 col-md-5 col-lg-5 text-right'})
        website = website[0].a.attrs['href']
        #print(website)
        
        address = element.findAll('div', {'class': 'col-xs-5 col-sm-5 col-md-5 col-lg-5'})
        address = address[0].contents[1::2]
        for flag in address:
            addr += flag.text + ', '
        #print(addr)
        
        telephone = element.findAll('div', {'class': 'col-xs-10 col-sm-10 col-md-9 col-lg-9'})
        telephone = telephone[0].contents[1::2]
        k = 0
        for tel in telephone:
            if(k == 0):
                email = tel.text
            else:
                tele.append(tel.text)
            k +=1
        #print(email)
        #print(tele)
        k = 0
        l = len(tele)
        for x in tele:
            if(k != l - 1):
                telep += str(x) + ' | '
            else:
                telep += str(x)
            k += 1
        file.write(name.replace(',', '') + ',' + email.replace(',', '') + ',' + telep.replace(',', '') + ',' + website.replace(',', '') + ',' + addr.replace(',', '') + '\n')
        print(name.replace(',', '') + ',' + email.replace(',', '') + ',' + telep.replace(',', '') + ',' + website.replace(',', '') + ',' + addr.replace(',', '') + '\n')
file.close()



#name = element.findAll('div', {'class': 'col-xs-7 col-sm-7 col-md-7 col-lg-7 text-left'})
# name[0].contents[1].text

#website = elements[0].findAll('div', {'class': 'col-xs-5 col-sm-5 col-md-5 col-lg-5 text-right'})
#website[0].a.attrs['href']

#address = elements[1].findAll('div', {'class': 'col-xs-5 col-sm-5 col-md-5 col-lg-5'})
# address = address[0].contents[1::2]
#traverse address to get Address

#telephone = elements[0].findAll('div', {'class': 'col-xs-10 col-sm-10 col-md-9 col-lg-9'})
#telehone = telephone[0].contents[1::2] after index 1 telephone

#email = elements[0].findAll('div', {'class': 'col-xs-10 col-sm-10 col-md-9 col-lg-9'})
#email = email[0].contents[1::2] first index is email
