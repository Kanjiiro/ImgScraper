#!/usr/bin/python3

from tqdm import tqdm
import sys
from bs4 import BeautifulSoup
import urllib.request

site_url = "URL TO INSERT HERE"


def getpage(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    request = urllib.request.Request(
        url, None, headers)  # The assembled request
    response = urllib.request.urlopen(request)
    data = response.read()  # The data u need
    return data


def findlinks(data):
    global site_url
    soup = BeautifulSoup(data, 'html.parser')
    link = soup.findAll("div", {"class": "link"})
    href = []
    for link in soup.find_all('a'):
        ok_site = link.get('href')
        if len(ok_site) > 36:
            if ok_site[:40] != site_url:
                href.append(ok_site)
        else:
            continue
    return set(href)


def model_name(url):
    name = url[35:len(url) - 1]
    m_name = name
    return m_name

# getting the pics url


def pics_url(url):
    m_name = model_name(url)
    hrefs = findlinks(getpage(url))
    pics_page_url = []
    for models_url in hrefs:
        if models_url[35:len(url) - 1] == m_name:
            pics_page_url.append(models_url)
    return pics_page_url


def main():
    global site_url
    # get page  links
    url = str(sys.argv[1])
    hrefs = findlinks(
        getpage(site_url + url))

###############################

    # get pics links
    url_pics = list(hrefs)
    for i in tqdm(url_pics):
        ...
        f = open("links.txt", "a+")
        for img_urls in pics_url(i):
            f.write(img_urls + ' \n')
        f.close()


###############################
if __name__ == "__main__":
    main()
