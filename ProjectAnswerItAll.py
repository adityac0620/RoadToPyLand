import bs4
from bs4 import BeautifulSoup as soup
import lxml
from urllib.request import urlopen as uo

# Declaring the url and getting the full webpage using urllib. 
url=input("Enter a link to the topic's WikiPedia page : ")
uclient=uo(url)
page_html=uclient.read()
uclient.close()

#Using beautiful soup to parse the html page into required form
page_soup = soup(page_html, "html.parser")
# Finding all paragraphs in "bodyContent" div's of the "content" div. 
datadump=page_soup.body.find("div", {'id':'content'}).find("div",{'id':'bodyContent'}).find_all("p")

#filtering out all the reference tags in the wikipedia page
for udd in datadump:
    m=udd.find_all("sup")
    if m != None:
        for i in m:
            i.string=""

# Printing the collected info.
for dd in datadump:
    onlyTextDump=dd.get_text()
    print(onlyTextDump)