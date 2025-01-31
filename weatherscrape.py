#Create a program to store the outside temperature, the daily high, and daily low, every 
# hour. Start by printing the data to the terminal before modifying your program to send 
# your data to an output file. We will set these up so they run for at least a full 48 
# hours.port requests

import requests
from bs4 import BeautifulSoup
import time
url = "https://forecast.weather.gov/MapClick.php?lat=39.6127&lon=-105.0162"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

while True:
    try:
        high = 0
        low = 0
        info = soup.find('body')
        info = info.find('div', id='seven-day-forecast')
        info = info.find('div', id='seven-day-forecast-body')
        info = info.find('div', id='seven-day-forecast-container')
        info = info.find('ul', id='seven-day-forecast-list')
        info = info.find('li')
        list = info.find_all('p')
        for l in list:
            print(l)
            if "High" in l:
                high = l
            elif "Low" in l:
                low = l
        print(high)
        print(low)
    except RuntimeError:
        pass
    time.sleep(3)
