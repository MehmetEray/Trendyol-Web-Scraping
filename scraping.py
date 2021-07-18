from selenium import webdriver
import time
from bs4 import BeautifulSoup

sourceURL = "https://www.trendyol.com/saat-x-c34"

clocks_dict = {}
clocks_brands = []
clocks_prices = []
# start web browser
browser=webdriver.Firefox()

# get source code
browser.get(sourceURL) 
html = browser.page_source
time.sleep(2)

soup = BeautifulSoup(html, 'html.parser')

for clocks in soup.find_all("div",{"class":"prdct-desc-cntnr-ttl-w two-line-text"}):
    clock_brands = clocks.find("span",{"class":"prdct-desc-cntnr-ttl"}).text
    clocks_brands.append(clock_brands)

for clocks_price in soup.find_all("div",{"class":"prc-box-sllng"}):
    clocks_prices.append(clocks_price.text)

for key in clocks_brands:
    for value in clocks_prices:
        clocks_dict[key] = value
print(str(clocks_dict))
# close web browser
browser.close()
