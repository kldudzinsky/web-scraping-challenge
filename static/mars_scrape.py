
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return browser = Browser('chrome', **executable_path, headless=False)
def scrape():
#Nasa News Site: visit 
    nasa_url= 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)

    html=browser.html
    soup=BeautifulSoup(html, "html.parser")

    news_title = soup.findAll('div', class_='content_title')[1].text
    news_p = soup.find('div', class_='article_teaser_body').text

    from pprint import pprint
    pprint(news_p)

    mars={"News_title":news_title, "Description":news_p}


# JPL mars-Featured Image

    jpl_url="https://www.jpl.nasa.gov/images/?search=&category=Mars"
    browser.visit(jpl_url)

    cards=browser.find_by_css('.BaseImage')
    cards

    [x.text for x in cards]
    cards[0].click()

    soup=BeautifulSoup(browser.html,'html.parser')
    images=soup.find_all('img', class_="BaseImage")[0]

    mars_image=images

##FACTS

    url_facts=url="https://space-facts.com/mars/"
    browser.visit(url_facts)

    html_facts=browser.html
    soup_facts=BeautifulSoup(html_facts,'html.parser')
    tables=pd.read_html(url)
    tables

    mars_facts_df=tables[0]
    mars_facts_df
    #astrogeology   
    astr_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(astr_url)
    html=browser.html
    soup=BeautifulSoup(browser.html,'html.parser')
    main_url="https://astrogeology.usgs.gov"
    image_urls=[]
    mars_data=[]

    items=soup.find_all('div',class_='item')
    pprint(items)

    # Loop through the items previously stored
    for item in items:
        title = item.find('h3').text
        img_url = item.find('a', class_='itemLink product-item')['href']
        browser.visit(main_url + img_url)
        img_html = browser.html
        soup = BeautifulSoup(img_html, 'html.parser')
        img_url = main_url + soup.find('img', class_='wide-image')['src']
        image_urls.append({"title":title,"image":img_url})
    browser.quit()

    return(image_urls)