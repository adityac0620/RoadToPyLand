import bs4
from bs4 import BeautifulSoup as soup
import lxml
from urllib.request import urlopen as uo

# Declaring the url and getting the full webpage using urllib. 
url="https://en.wikipedia.org/wiki/Apache_License"
uclient=uo(url)
page_html=uclient.read()
uclient.close()

#Using beautiful soup to parse the html page into required form
page_soup = soup(page_html, "html.parser")
# Finding all paragraphs in "bodyContent" div's of the "content" div. 
datadump=page_soup.body.find("div", {'id':'content'}).find("div",{'id':'bodyContent'}).find_all("p")
# Printing the collected info.
for dd in datadump:
    onlyTextDump=dd.get_text()
    print(onlyTextDump)
