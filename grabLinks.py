from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import requests
import io, os
import time
import pickle
DRIVER_PATH = "C:\Program Files\Google\chromedriver.exe"
wd = webdriver.Chrome(executable_path=DRIVER_PATH)
page = 0
allProd = []
while page < 1193:

    link = "https://www.vinmonopolet.no/search?q=:alcohol-desc:visibleInSearch:true&searchType=product&currentPage=" + str(page)
    wd.get(link)
    with open('links.pkl', 'wb') as f:
        pickle.dump(allProd, f)
    time.sleep(2)
    drinks = wd.find_elements_by_class_name("product-item__image-container")
    for drink in drinks:
        prod = drink.get_attribute("href")
        print(prod)
        allProd.append(prod)




    page = page + 1
