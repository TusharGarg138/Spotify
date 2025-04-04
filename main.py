import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

year = input("Which year you want to trvael, format: YYYY-MM-DD:\n")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(URL)
website_html = response.text
#print(website_html)

