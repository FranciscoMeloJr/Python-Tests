def view_content(url="http://www.g1.globo.com"):
    import urllib.request
    import html2text
    from bs4 import BeautifulSoup

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
    #print(soup.prettify())

    #Title:
    print(soup.title.string)

view_content()