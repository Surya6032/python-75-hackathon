import requests
from bs4 import BeautifulSoup
import re

"""
To handle routing to insecure page i.e navigatiing to 'http' requests which donot 
have SSL certificates and are consideres to be insecure.

The below lines are added to suppress the below error:
------------------------------------------------------
InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.

"""
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

""" 
    Filtering URLs from the mixed collection of href's contaings routes, images and URLs based on a Regular Expression.
"""


def url_validation(link):
    urlregex = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return re.match(urlregex, str(link)) is not None


#Making request to our desired Page on WikiPedia
def deadLinkFiner(url):
    page = requests.get(str(url))  # The URL is of our choice

    set = []
    urls = []
    valid_urls = []
    dead_links = []
    conn_refused = []
    forbidden_urls = []

    soup = BeautifulSoup(page.content, 'html.parser')
    set = soup.find_all('a')

    # To get the href from the collected Hyperlinks
    for i in set:
        urls.append(i.get('href'))

    # Applying URL validation and Holding together all the valid URLs in a list.
    for i in urls:
        if url_validation(i):
            valid_urls.append(i)
    """
    Making request to all the valid URLs.
    If the URL gives us a status-code, 200. Then it's a Dead Link. 
    If the URL gives us a status-code, 403. Then its a Forbidden Link.

    """
    print("Dead Links: ")
    for i in valid_urls:
        try:
            temp_page = requests.get(i, verify=False)
        except:
            conn_refused.append(i)
        if (temp_page.status_code == 403):
            forbidden_urls.append(i)
        elif not (temp_page.status_code == 200):
            print("* ", i)
            dead_links.append(i)

    # Finally printing out all the Dead Links,Forbidden Links and the URLs that are taking too long to respond.

    if len(dead_links) == 0:
        print("No Dead links found.")
    else:
        print("Number of Dead links: ", len(dead_links))
    if (len(conn_refused) != 0):
        print('Urls which refused connection or taking long time:')
        for i in conn_refused:
            print("* ", i)
    if(len(forbidden_urls) != 0):
        print('Forbidden URLs:')
        for i in forbidden_urls:
            print("* ", i)


link = input("Enter your URL")
deadLinkFiner(link)
