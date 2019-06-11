# Start with code from urlXKCD, and modify as necessary
# urlSubnorm uses re
# Will likely have to add more variables

import requests
import os
import re
import bs4  # beautifulSoup4
from htmlCreator import buildComicPage


def urlBuild(urlFirstPage, filename, urlMain, urlnextBase, nextTag, nextAttr, nextStr, nextLinkParent):
    url = urlFirstPage
    writeURL = True
    pagecount = 0
    i = 0

    if os.path.isfile(os.path.join('webcomic', filename)):
        fileExists = True
    else:
        fileExists = False

    if fileExists:
        with open(os.path.join('webcomic', filename), 'r') as f:
            lines = f.read().splitlines()
            pagecount = len(lines)
            if pagecount > 0:
                writeURL = False
                url = lines[pagecount - 1]

    if len(nextTag) != len(nextAttr) or len(nextTag) != len(nextStr):
        print("Search conditions length mismatch")
        return pagecount
    searchLength = len(nextTag)

    while not url.endswith('#') and not url.endswith('zzzbreak'):  # on latest page url under 'Next' button ends with '#'
        # Download page
        print('Finding page %s...' %url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features='html.parser')

        if writeURL:
            try:
                comicFile = open(os.path.join('webcomic', filename), "a")
                comicFile.write(url + "\n")
                comicFile.close()
            except IOError:
                print("Error opening comic file: " + filename)
                exit(-1)

            i += 1
        else:
            writeURL = True

        # Get the Next button's URL
        nextTemp = None
        j = 0
        while nextTemp is None:
            if j < searchLength:
                #nextTemp = soup.find(nextTag1, rel="next")
                nextTemp = soup.find(nextTag[j], {nextAttr[j]: re.compile(nextStr[j])})
            else:
                print("next link couldn't be found")
                print("last found page: " + url)
                break
            j += 1

        if nextTemp is None:
            nextPage = 'zzzbreak'
        else:
            if nextLinkParent:
                nextLink = nextTemp.parent
            else:
                nextLink = nextTemp
            nextPage = nextLink.get('href')

        url = urlnextBase + nextPage

    pagecount = pagecount + i
    print('Done. Current Pagecount: ' + str(pagecount))

    #htmlXkcd(pagecount, filename)
    buildComicPage(pagecount, filename)

    return pagecount


if __name__ == "__main__":
    urlFirstPage = 'http://xkcd.com/1/'
    filename = "xkcd"
    urlMain = "http://www.xkcd.com/"
    nextLinkParent = False
    urlnextBase = 'http://xkcd.com'
    nextTag = []
    nextAttr = []
    nextStr = []
    nextTag.append("a")
    nextAttr.append("rel")
    nextStr.append("next")

    os.makedirs('webcomic', exist_ok=True)
    urlBuild(urlFirstPage, filename, urlMain, urlnextBase, nextTag, nextAttr, nextStr, nextLinkParent)
