# Start with code from urlXKCD, and modify as necessary
# urlSubnorm uses re
# Will likely have to add more variables

import requests
import os
import re
import bs4  # beautifulSoup4
from htmlCreator import buildComicPage

# Set user agent, as requests default agent is blocked in some cases
# This agent is a "Linux-based PC using a Firefox browser" from https://deviceatlas.com/blog/list-of-user-agent-strings
sUserAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'

def urlBuild(urlFirstPage, filename, urlMain, urlBases, nextTag, nextAttr, nextStr, nextLinkParent,
             searchend = '.us.k12.edu', baseChanges = False):
    url = urlFirstPage
    urlPrev = ''
    numBases = len(urlBases)
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

    if numBases < 1:
        print("No Base defined, assuming full URL in next link")
        urlBases.append("")
        urlnextBase = urlBases[0]
        numBases = 1
    elif not writeURL and numBases > 1:
        m = 0
        while m < numBases:
            if url.startswith(urlBases[m]):
                urlnextBase = urlBases[m]
                break
            m += 1
    else:
        urlnextBase = urlBases[0]

    if len(nextTag) != len(nextAttr) or len(nextTag) != len(nextStr):
        print("Search conditions length mismatch")
        return pagecount
    searchLength = len(nextTag)

    # Stop if the next url is the "searchend", or no next URL is found, or next URL is the same as the previous URL
    while not url.endswith(searchend) and not url.endswith('zzzbreak') and urlPrev != url:
        # Download page
        print('Finding page %s...' %url)
        try:
            res = requests.get(url, headers={"User-Agent":sUserAgent})
        except requests.ConnectionError as err:
            try:
                res = requests.get(url, verify=False)
            except:
                print(" *** ")
                print(err)
                print(" *** ")
                break
        except requests.exceptions.RequestException as err:
            print(" *** ")
            print(err)
            print(" *** ")
            break

        try:
            res.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(" *** ")
            print(err)
            print(" *** ")
            break

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
                if nextAttr[j] == 'text':
                    nextTemp = soup.find(nextTag[j], text=nextStr[j])
                elif nextAttr[j] == 'class' or nextAttr[j] == 'class_':
                    nextTemp = soup.find(nextTag[j], class_=nextStr[j])
                else:
                    nextTemp = soup.find(nextTag[j], {nextAttr[j] : re.compile(nextStr[j])})
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
            if nextPage == "" or nextPage is None:
                nextPage = 'zzzbreak'

        # Prevent loop if "Next" comic is the same as the last comic
        urlPrev = url

        if baseChanges and nextPage.startswith("http"):
            k = 0
            while k < numBases:
                if nextPage.startswith(urlBases[k]):
                    print("New base found: " + urlBases[k])
                    urlnextBase = urlBases[k]
                    url = nextPage
                    break
                k += 1
            if k == numBases:
                print("No matching base URL. Cannot proceed till new base is added to array")
                print("Previous base: " + urlnextBase)
                print("Latest url (not added): " + nextPage)
                print("Current Pagecout: " + str(pagecount))
                buildComicPage(pagecount, filename)
                return pagecount
        else:
            # Trim leading ".." from certain partial links (EX. "../vol1/1.php")
            if nextPage.startswith("../"):
                nextPage = nextPage[2:]

            url = urlnextBase + nextPage

    pagecount = pagecount + i
    print('Done. Current Pagecount: ' + str(pagecount))

    buildComicPage(pagecount, filename)

    return pagecount


if __name__ == "__main__":
    nextTag = []
    nextAttr = []
    nextStr = []
    urlBase = []
    comicname = "A Redtail's Dream"
    filename = "redtail"
    urlMain = "http://www.minnasundberg.fi/comic/recent.php"
    urlFirstPage = "http://www.minnasundberg.fi/comic/page00.php"
    nextTag.append("img")
    nextAttr.append("src")
    nextStr.append(".*anext[.]jpg")
    urlBase.append("http://www.minnasundberg.fi/comic/")
    nextLinkParent = True
    baseChange = False

    os.makedirs('webcomic', exist_ok=True)
    urlBuild(urlFirstPage, filename, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, baseChanges=baseChange)
