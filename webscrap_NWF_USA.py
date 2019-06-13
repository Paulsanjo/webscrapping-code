import requests as rq
import pandas as pd
from bs4 import BeautifulSoup
url = input('enter the url of National Weather Forecast to scrap--> ')
page = rq.get(url)
soup = BeautifulSoup(page.content,'lxml')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_ = 'tombstone-container')
items.pop(0)
detailed_forecast = soup.find_all(class_='row-forecast')
period_names = [item.find(class_ = 'period-name').get_text() for item in items]
short_desc = [item.find(class_ = 'short-desc').get_text() for item in items]
temp = [item.find(class_ = 'temp').get_text() for item in items]
label = [iteem.find(class_ = 'forecast-label').get_text() for iteem in detailed_forecast]
text = [iteem.find(class_ = 'forecast-text').get_text() for iteem in detailed_forecast]
weather_forecast = pd.DataFrame({
    'Forecast-Label':label,
    'Forecast-Text':text,
})

weather_data = pd.DataFrame({
    'Period':period_names,
    'Description':short_desc,
    'Temperature':temp,
})
wd = input('enter the weather data name in format like- sampledata.csv  - -> ')
wf = input('enter the weather forecast name in format like- sampleforecast.csv  - -> ')
weather_data.to_csv(wd)
weather_forecast.to_csv('weather-forcast.csv')