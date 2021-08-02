import requests
import os
import re
import bs4  # beautifulSoup4
from htmlCreator import buildComicPage

# Set user agent, as requests default agent is blocked in some cases
# This agent is a "Linux-based PC using a Firefox browser" from https://deviceatlas.com/blog/list-of-user-agent-strings
sUserAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'


def urlBuild(urlFirstPage, filename, urlMain, urlBases, nextTag, nextAttr, nextStr, nextLinkParent,
             search_end='.us.k12.edu', baseChanges=False):
    url = urlFirstPage
    urlPrev = ''
    numBases = len(urlBases)
    writeURL = True
    page_count = 0
    i = 0
    isbutton = False

    if os.path.isfile(os.path.join('webcomic', filename)):
        fileExists = True
    else:
        fileExists = False

    if fileExists:
        with open(os.path.join('webcomic', filename), 'r') as f:
            lines = f.read().splitlines()
            page_count = len(lines)
            if page_count > 0:
                writeURL = False
                if lines[page_count - 1] == "zzzENDzzz":
                    page_count -= 1
                    url = lines[page_count]
                else:
                    url = lines[page_count - 1]

    urlnextBase = urlBases[0]  # was an else, moved to remove IDE warnings
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

    if len(nextTag) != len(nextAttr) or len(nextTag) != len(nextStr):
        print("Search conditions length mismatch")
        return page_count
    searchLength = len(nextTag)

    # Stop if the next url is the "search_end", or no next URL is found, or next URL is the same as the previous URL
    while not url.endswith(search_end) and not url.endswith('zzzENDzzz') and urlPrev != url:
        # Download page
        print('Finding page %s...' % url)
        try:
            res = requests.get(url, headers={"User-Agent": sUserAgent})
        except requests.ConnectionError as err1:
            try:
                res = requests.get(url, verify=False)
            except Exception as err2:
                print(" *** ")
                print(err1)
                print(err2)
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
                    nextTemp = soup.find(nextTag[j], {nextAttr[j]: re.compile(nextStr[j])})

                if nextTag[j] == 'button':
                    isbutton = True
                else:
                    isbutton = False
            else:
                print("next link couldn't be found")
                print("last found page: " + url)
                break
            j += 1

        if nextTemp is None:
            nextPage = 'zzzENDzzz'
        else:
            if nextLinkParent:
                nextLink = nextTemp.parent
            else:
                nextLink = nextTemp

            if isbutton:
                nextPage = nextLink.get('onclick')[15:-1]
            else:
                nextPage = nextLink.get('href')

            if nextPage == "" or nextPage is None:
                nextPage = 'zzzENDzzz'

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
                print("Current Page Count: " + str(page_count))
                buildComicPage(page_count, filename)
                return page_count

        url = urlnextBase + nextPage

    page_count = page_count + i
    print('Done. Current Page Count: ' + str(page_count))

    buildComicPage(page_count, filename)

    return page_count


if __name__ == "__main__":
    nextTag = []
    nextAttr = []
    nextStr = []
    urlBase = []
    comic_name = "Tripp"
    file_name = "tripp"
    urlMain = "https://web.archive.org/web/20150506105057/http://www.trippcomic.com/home"
    urlFirstPage = "https://web.archive.org/web/20150507152639/http://www.trippcomic.com/archives/archive/poet-b5e016f"
    nextTag.append("a")
    nextAttr.append("rel")
    nextStr.append("next")
    nextLinkParent = False
    baseChange = False

    os.makedirs('webcomic', exist_ok=True)
    urlBuild(
        urlFirstPage, file_name, urlMain, urlBase, nextTag, nextAttr, nextStr, nextLinkParent, baseChanges=baseChange)
