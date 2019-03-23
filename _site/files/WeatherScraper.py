#!/usr/bin/env python3
# -*- coding: utf-8 -*-t

################################################################
# Web page requests can be made with the requests package
################################################################

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"user-agent": "Webscraper Demo"}
page = requests.get("https://weather.com/weather/5day/l/USCT0260:1:US", headers = headers)

if page.status_code != requests.codes.ok :
    print("Request was not successful, status code:", page.status_code)
    exit()
    
# Parse page using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find("table", {"class":"twc-table"})
trs = table.find_all("tr")
days = []
temps = []
for rows in trs[1:] :
    date = rows.find("span", {"class":"date-time"})
    temp = rows.find("td", {"class":"temp"})
    theDate = date.string
    theHighTemp = temp.span.contents[0]
    print(theDate, ": ", theHighTemp, sep = "")
    if theHighTemp.isdigit() :
        days.append(theDate)
        temps.append(int(theHighTemp))
    

# create a data frame (a table) by specifying a dictionary
# with column names as keys and corresponding column values
# as values
df= pd.DataFrame(data = {"days":days, "hi_temp":temps})
df

# generate a bar graph of high temperatures for each day
# set rot (rotate) to 0 so bar labels are horizontal
plt = df.plot.bar(x = "days", y = "hi_temp", 
            title = "Willimantic High Temps, next 5 days",
            legend = False, rot = 0)

plt.set_xlabel("Day of the Week")
plt.set_ylabel("Temperature (Degrees Fahrenheit)")



'''
########################################################################
# Note: the wordcloud package has to be installed for this code to work
########################################################################
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# get Willimantic weather descriptions (the text only) and store 
# as a single string
descriptions = table.find_all("td", {"class": "description"})
descriptions = [d.text for d in descriptions]
descriptions = " ".join(descriptions)

#generate the word cloud
wordcloud = WordCloud(
        background_color = 'black',
        stopwords = STOPWORDS 
).generate(descriptions)

plt.imshow(wordcloud)
plt.show()
'''
