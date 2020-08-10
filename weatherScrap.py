import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=36.3741&lon=-119.2702#.XzGPLe_ivDc")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")

items = week.find_all(class_="tombstone-container")

period_names = [item.find(class_="period-name").get_text() for item in items]
short_desc = [item.find(class_="short-desc").get_text() for item in items]
temp = [item.find(class_="temp").get_text() for item in items]

weather_stuff = pd.DataFrame(
    {
        "period": period_names,
        "short_descriptions": short_desc,
        "temperature": temp,
    }
)

weather_stuff.to_csv("weather.csv")


