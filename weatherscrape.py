#Create a program to store the outside temperature, the daily high, and daily low, every 
# hour. Start by printing the data to the terminal before modifying your program to send 
# your data to an output file. We will set these up so they run for at least a full 48 
# hours.port requests

import requests
from bs4 import BeautifulSoup
import time
from datetime import date
from datetime import datetime
url = "https://forecast.weather.gov/MapClick.php?lat=39.6127&lon=-105.0162"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
denver = open("Denver.txt", 'a')

while True:
    #Open file
    with open('Denver.txt') as file:
        denver = open("Denver.txt", 'a')
    try:
        #Find Daily High and Lows
        info = soup.find('body')
        info = info.find('div', id='seven-day-forecast')
        info = info.find('div', id='seven-day-forecast-body')
        info = info.find('div', id='seven-day-forecast-container')
        info = info.find('ul', id='seven-day-forecast-list')
        info = info.find_all('li')
        for i in info:
            list = i.find_all('p')
            for l in list:
                if "temp temp-high" in str(l):
                    high = str(l)
                    high = high[32:37]
                elif "temp temp-low" in str(l):
                    low = str(l)
                    low = low[30:35]

        #Find current temp
        info = soup.find('body')
        info = info.find('div', id='current-conditions')
        info = info.find('div', id='current-conditions-body')
        info = info.find('div', id='current_conditions-summary')
        info = info.find_all('p')
        for i in info:
            if "myforecast-current-lrg" in str(i):
                current = str(i)
                current = current[34:38]

        #Find date
        dateToday = date.today()

        #Find time
        clockNow = datetime.now()

        #Add information to file
        #print(f"{clockNow}, {dateToday}, {current}, {high}, {low}")
        denver.write(f"{clockNow}, {dateToday}, {current}, {high}, {low}")
    except:
        pass
    
    time.sleep(1440)
