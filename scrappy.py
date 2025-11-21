#Name: Kalia Hudson
#Date: 09-24-25
#Program Name: Scrappy
#Program Purpose: To parse websites html for certain data. Data could include page
#titles, keywords, page elements, etc.

import requests
from bs4 import BeautifulSoup
import json

with open('config.json') as f:
    #Opening the config.json file
    
    #Saving content in "config"
    config = json.load(f)

#Optional print of json file contents
print(config)

#Define headers and target url
HEADERS = config['headers']
TARGET_URL = config['base_url']

def fetch_html(url):
    #Fetching the html
    response = requests.get(url, headers = HEADERS)

    print("Status Code:")
    if response.status_code == 200:
        #checking status code
        print("Access Granted")
    elif response.status_code == 403:
        print("Access Forbidden")
    elif response.status_code == 404:
        print("Page Not Found")
    else:
        print("Error")
    return response.text

def parse_html(html):
    #Using the lxml parser for speed and accuracy
    soup = BeautifulSoup(html, "lxml")
    #Printing the page title
    print("Page title: ", soup.title.text.strip())
    return soup

def extract_data(soup):
    #Extracting all H1 tags
    h1_tags = soup.find_all('h1')
    print("\nH1 Tags:")

    #Creating a list to hold h1 tags.
    cleanedTags = []

    for tag in h1_tags:
        cleanedTags.append(tag.text.strip())

    for tag in cleanedTags:
        print(tag)

    return cleanedTags
    
#Call to fetch raw html
rawHtml = fetch_html(TARGET_URL)

#Call to turn raw into soup
siteSoup = parse_html(rawHtml)

#Extracting specific data
extractedList = extract_data(siteSoup)

print("Extracted list", extractedList)



