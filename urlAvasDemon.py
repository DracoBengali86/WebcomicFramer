import requests
import os
#import re
import bs4  # beautifulSoup4
from htmlCreator import buildComicPage

#latestPage = '2382'


def urlBuild(urlFirstPage, filename, urlMain):
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


    #Main URL uses an event to load latest page instead of an href
    #will need to work out how to read the event (or manually add pages)

    try:
        res = requests.get(urlMain)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features='html.parser')
        latestLink = soup.find("img",src="latest.png").parent
        latestPage = latestLink.get('href')[-4:]
        pastLatest = str(int(latestPage) + 1).zfill(4)
    except TypeError:
        print("***Ava's Demon is currently broken***")
        print('***Current Pagecount: ' + str(pagecount) + '***\n')
        try:
            buildComicPage(pagecount, filename, True)
        except:
            print("building comic page failed!")
            return 0
        return pagecount

    while not url.endswith(pastLatest):  # on latest page url under 'Next' button ends with '#'
        # Download page
        print('Finding page %s...' %url)
        res = requests.get(url)
        res.raise_for_status()

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
        nextLink = url[-4:]
        nextPage = int(nextLink) + 1
        nextLink = str(nextPage).zfill(4)

        #url = 'http://www.AvasDemon.com/pages.php?page=' + nextLink
        url = 'http://www.avasdemon.com/pages.php?page#' + nextLink

    pagecount = pagecount + i
    print('Done. Current Pagecount: ' + str(pagecount))

    buildComicPage(pagecount, filename, True)

    return pagecount


if __name__ == "__main__":
    urlFirstPage = 'http://www.AvasDemon.com/pages.php?page=0001'
    #url = 'http://www.AvasDemon.com/pages.php#0001'
    urlMain = 'http://www.AvasDemon.com'
    filename = 'AvasDemon'

    os.makedirs('webcomic', exist_ok=True)
    urlBuild(urlFirstPage, filename, urlMain)
