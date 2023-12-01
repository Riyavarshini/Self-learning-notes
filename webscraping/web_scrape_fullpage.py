from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Function to extract Book Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"class":'ux-textspans ux-textspans--BOLD'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Book Price
def get_price(soup):

    try:
        price = soup.find("div", attrs={"class":'x-price-primary'}).find("span",attrs={"class":'ux-textspans'}).text.split(' ')[1]

    except AttributeError:
            price = ""

    return price

# Function to extract Book Rating
def get_rating(soup):

    try:
        rating = soup.find("span",attrs ={"class":'ux-summary__start--rating'}).find("span",attrs={"class":'ux-textspans'}).text
    
    except AttributeError:
            rating = ""
    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span",attrs ={"class":'ux-summary__count'}).find("span",attrs={"class":'ux-textspans'}).text

    except AttributeError:
        review_count = ""

    return review_count

# Function to extract Condition of book
def get_condition(soup):
    try:
        condition = soup.find("span", attrs={"data-testid":'ux-textual-display'}).find("span",attrs={"class":'ux-textspans'}).text

    except AttributeError:
        condition = ""

    return condition

# Function to extract Seller Name
def get_seller_name(soup):
    try:
        seller_name = soup.find("div",attrs ={"class":'d-stores-info-categories__container__info__section'}).find("h2",attrs={"class":'d-stores-info-categories__container__info__section__title'}).get('title')

    except AttributeError:
        seller_name = ""

    return seller_name

# Function to extract Seller rating
def get_seller_rating(soup):
    try:
        seller_rating = soup.find("div",attrs ={"class":'d-stores-info-categories__container__info__section__item'}).find("span",attrs={"class":'ux-textspans ux-textspans--BOLD'}).text
        
    except AttributeError:
        seller_rating = ""

    return seller_rating


if __name__ == '__main__':

    # add your user agent 
    HEADERS = ({'User-Agent':'Add you user_agent', 'Accept-Language': 'en-US, en;q=0.5'}) 

    # The webpage URL
    URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=books&_sacat=0&LH_TitleDesc=0&_odkw=language+books&_osacat=0"
    
    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    tags = soup.find_all("a", attrs={'class':'s-item__link'})

    # Store the tags
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in tags:
            links_list.append(link.get('href'))

    d = {"title":[], "price":[], "rating":[], "no_of_reviews":[],"condition":[], "seller_name":[], "seller_rating":[]}
    
    # Loop for extracting product details from each link 
    for link in links_list:
        product_webpage = requests.get(link, headers=HEADERS)

        new_soup = BeautifulSoup(product_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['no_of_reviews'].append(get_review_count(new_soup))
        d['condition'].append(get_condition(new_soup))
        d['seller_name'].append(get_seller_name(new_soup))
        d['seller_rating'].append(get_seller_rating(new_soup))

    
    ebay_df = pd.DataFrame.from_dict(d)
    ebay_df['title'].replace('', np.nan, inplace=True)
    ebay_df = ebay_df.dropna(subset=['title'])

  print(ebay_df)
