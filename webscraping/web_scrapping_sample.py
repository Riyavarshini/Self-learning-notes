# In this code we scrape details of one books
# STEP 1: Import required libraries

from bs4 import BeautifulSoup # BeautifulSoup is used to parse html code and find elements essential for webscrapping.
import requests # Send HTTPS requests from local PC to Amazon,ebay like servers.
import pandas as pd # Used to store contents in dataframes and get csv files.

# STEP 2: GET URL OF YOUR CHOICE. I AM USING EBAY PLATFORM TO SCRAP BOOKS AVAILABLE.
# Go to ebay.com. Search 
URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=books&_sacat=0&LH_TitleDesc=0&_odkw=language+books&_osacat=0"

# STEP 3: Define HTTP Headers

# Headers let the client and the server pass additional information with an HTTP request or response. User-Agent is an important component of the Header.
# User-Agent: Including a User-Agent header helps websites identify your scraping bot and can make it appear more like a legitimate user's request.
# Search for "My user agent" in browser. It displays your system user agent. Copy and paste it.
# The Accept-Language header indicates the preferred language of the client with a fallback option for English (en;q=0.5).

HEADERS = ({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

# STEP 4: Pass url,headers to get request
webpage = requests.get(URL, headers=HEADERS)
# Check if you get response [200]
print(webpage)
#If response [503] means wait for some time and retry.

# View content
print(webpage.content)

#Content is in byte datatype
print(type(webpage.content))

# STEP 5: Convert byte to proper HTML code using BeautifulSoup
# pass content of webpage 
soup = BeautifulSoup(webpage.content,"html.parser") # "html.parser" is the parser used for parsing the HTML content.
print(soup)
# HTML CODE STARTS WITH <!DOCTYPE html> header

# After this we need to parse through this html code and find the required attribute to retrieve the data.

# STEP 6: # FETCH LINKS AS LISTS OF TAG OBJECTS
# Now in our ebay link, we have list of products. each product link to new page which shows product details completely.
# Now we need to fetch link to access.
# Refer HTML_attribute_retrieval.md file for how to get elements.

# soup.find_all("tag_name", attrs = {'element_name':'element_id'})
tags = soup.find_all("a", attrs={'class':'s-item__link'})
print(tags)

# In this code we scrape details of one books, so we use only one link.
print(tags[1]) # any object

# STEP 7: We need to extract href from <a> .... </a> from above tag object
link = tags[1].get('href')
print(link) # Make sure the link extracted is complete and working. Else you need an extra step to add missing part of link.

# STEP 8: Again we need to get request for this new page to visit, convert content of webpage from byte to HTML
product_webpage = requests.get(link, headers=HEADERS)
print(product_webpage) # Check if you get response [200]
new_soup = BeautifulSoup(product_webpage.content, "html.parser")
print(new_soup)
# After this we need to parse through this html code and find the required attribute to retrieve the data.
# STEP 9: extract Details.
# a) Book title
title = new_soup.find("span", attrs={"class":'ux-textspans ux-textspans--BOLD'}).text.strip() # retrieves text part of <span>....</span> and trim white spaces before and after text.
print(title)
# b) Book condition
condition = new_soup.find("span", attrs={"data-testid":'ux-textual-display'}).find("span",attrs={"class":'ux-textspans'}).text
print(condition)

# c) price
price = new_soup.find("div", attrs={"class":'x-price-primary'}).find("span",attrs={"class":'ux-textspans'}).text.split(' ')[1]
print(price)

# d) rating
rating = new_soup.find("span",attrs ={"class":'ux-summary__start--rating'}).find("span",attrs={"class":'ux-textspans'}).text
print(rating)

# e) Number of reviews
# Here we have data inside sub-span so we use find twice <span>.....<span>......</span>..</span>
no_of_review = new_soup.find("span",attrs ={"class":'ux-summary__count'}).find("span",attrs={"class":'ux-textspans'}).text
print(no_of_review)

# f) Seller name
Seller_name = new_soup.find("div",attrs ={"class":'d-stores-info-categories__container__info__section'}).find("h2",attrs={"class":'d-stores-info-categories__container__info__section__title'}).get('title')
print(Seller_name)

# g) Seller rating
Seller_rating = new_soup.find("div",attrs ={"class":'d-stores-info-categories__container__info__section__item'}).find("span",attrs={"class":'ux-textspans ux-textspans--BOLD'}).text
print(Seller_rating)

# -------- HURRAY! SUCCESSFULLY SCRAPED A BOOK DETAILS ----------
# Find the other code file to scrape all book details from a page.

