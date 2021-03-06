import sys
import urllib.request
import html2text
from bs4 import BeautifulSoup

#Get Title
def get_title_kcs(url_kcs):
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content, features="html.parser")
    #soup = BeautifulSoup(open("test\solution.html"), "html.parser")
    return soup.title.string

#Get Content
def get_content(url_kcs="test\solution.html"):
    #content = urllib.request.urlopen(url).read()
    #soup = BeautifulSoup(content, features="html.parser")
    soup = BeautifulSoup(open("test\solution.html"), "html.parser")
    return soup.text

#Get Parsed Content
def parse_kcs(url="http://www.g1.globo.com"):
    dit_text = {}
    #req = urllib.request.Request('http://www.g1.com.br')
    #url = "http://www.g1.globo.com"
    try:
        soup = BeautifulSoup(open("test\solution.html"), "html.parser")
        #Print all as text:
        #print(soup.text)

        #Print all:
        #print(soup.prettify())

        # Title:
        dit_text['title'] = soup.title.string

        # Environment:
        dit_text['env'] = soup.find("section", class_="field_kcs_environment_txt").text

        # Issue:
        dit_text['issue'] = soup.find("section", class_="field_kcs_issue_txt").text

        # Resolution:
        dit_text['resolution'] = soup.find("section", class_="field_kcs_resolution_txt").text

        # Observation:
        dit_text['observation'] = soup.find("section", class_="field_kcs_observation_txt").text
        return dit_text
    except:
        e = sys.exc_info()[0]
        print(e)
        print("Exception opening content in Beautifulsoup")

#View Content
def view_content(url="http://www.g1.globo.com"):
    #req = urllib.request.Request('http://www.g1.com.br')
    #url = "http://www.g1.globo.com"
    try:
        content =  urllib.request.urlopen(url).read()
    except:
        print("Exception accessing" + url)

    try:
        soup = BeautifulSoup(content, features="html.parser")
    except:
        print("Exception opening content in Beautifulsoup")

    #All info:
    print(soup.prettify())

    #Title:
    print(soup.title.string)

dict_d = parse_kcs()
print(dict_d['env'])