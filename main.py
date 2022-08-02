from calendar import calendar
import requests
from bs4 import BeautifulSoup

print('Get Trading Economics page')
page = requests.get('https://tradingeconomics.com/pakistan/inflation-cpi', headers={'User-Agent': 'Mozilla/5.0'})

html = page.text

print('Creating Parse Object')
soup = BeautifulSoup(html, 'html.parser')

calendar = soup.find(id='calendar')

print(calendar.text)

print('Done')
