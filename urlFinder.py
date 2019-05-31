# Start with code from urlXKCD, and modify as necessary
# urlSubnorm uses re
# Will likely have to add more variables

import requests
import os
#import re
import bs4  # beautifulSoup4
from htmlCreator import buildComicPage


def urlBuild(urlFirstPage, filename, urlMain=None):
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

    while not url.endswith('#'):  # on latest page url under 'Next' button ends with '#'
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
        nextLink = soup.select('a[rel="next"]')[0]
        url = 'http://xkcd.com' + nextLink.get('href')

    pagecount = pagecount + i
    print('Done. Current Pagecount: ' + str(pagecount))

    #htmlXkcd(pagecount, filename)
    buildComicPage(pagecount, filename)

    return pagecount


if __name__ == "__main__":
    urlFirstPage = 'http://xkcd.com/1/'
    filename = "xkcd"

    os.makedirs('webcomic', exist_ok=True)
    urlBuild(urlFirstPage, filename)
