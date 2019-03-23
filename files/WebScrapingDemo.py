#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################
# Web scraping with Beautiful Soup (Note: we will use Beautiful
# Soup 4, or bs4). You may need to install this on your own
# computer. More information and some examples can be found 
# here: https://beautiful-soup-4.readthedocs.io/en/latest/#
################################################################

import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Webscraper Demo"}
page = requests.get("https://gdancik.github.io/CSC-360/data/notes/schedule.html", headers = headers)

if page.status_code != requests.codes.ok :
    print("Request was not successful, status code:", page.status_code)
    exit()

# parse the web page using Beatiful Soup, which creates a 
# BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# prettify converts the content into a nicely formatted string
print(soup.prettify())

################################################################
# The web page is stored as a 'tree', with elements either 
# strings or bs4 objects. Specify the tag name to get the FIRST 
# tag of that type
################################################################

# get the title of the page
soup.title

# get the first table on the page
soup.table

# get the page title
soup.title

# if an element has no children, .string will extract the text
soup.title.string
soup.title.string.strip()  # strip removes leading/trailing whitespace


# HTML elements have attributes (stored as dictionaries)

# get all attributes of the first div
soup.div.attrs

# get the 'class' of the first div
soup.div['class']


################################################################
# use .strings to get each string inside of a tag
# use .stripped_strings to remove whitespace
################################################################

# print the first 'tr' tag
print(soup.tr)

# print each string
for s in soup.tr.stripped_strings :
    print("tr string:", s)
    

################################################################
# searching the webpage, by tag name, class, etc (see examples)
# use find to get the first occurence 
# use find_all to get all occurences
################################################################

#finds the first tr element (same as soup.tr)
soup.find("tr")

#finds all tr elements
trs = soup.find_all("tr")
print("Number of table rows:", len(trs))
rowNum = 1
for row in trs :
    print("row #",rowNum)
    print(row)
    rowNum = rowNum + 1
    print()

# finds elements by id using named arguments
# (works for several attributes including id and href)    
soup.find_all(id = 'officeHours')

# for some attributes, you can specify a dictionary
# with the attribute and value

# finds all div elements with class = 'additional'
soup.find_all("div", {"class": "additional"})


################################################################
# Exercise: find and print the courses I teach
################################################################


