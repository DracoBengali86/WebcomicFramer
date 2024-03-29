import requests
import os
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
                if lines[pagecount - 1] == "zzzENDzzz":
                    pagecount -= 1
                    url = lines[pagecount]
                else:
                    url = lines[pagecount - 1]

    while not url.endswith('zzzENDzzz'):  # on latest page url under 'Next' button ends with '#'
        # Download page
        print('Finding page %s...' % url)
        try:
            res = requests.get(url)
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
            if j == 0:
                # find button with title = "Next Episode"
                nextTemp = soup.find("a", rel="next")
            else:
                print("next link couldn't be found")
                print("last found page: " + url)
                break
            j += 1

        if nextTemp is None:
            nextLink = 'https://q2qcomics.com/comic/zzzENDzzz'
        else:
            nextLink = nextTemp.get('href')

        url = nextLink

    pagecount = pagecount + i
    print('Done. Current Page Count: ' + str(pagecount))

    buildComicPage(pagecount, filename)

    return pagecount


if __name__ == "__main__":
    urlFirstPage = 'https://q2qcomics.com/comic/q2q1/'
    filename = 'q2qcomic'

    os.makedirs('webcomic', exist_ok=True)
    urlBuild(urlFirstPage, filename)
