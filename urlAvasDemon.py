import requests
import os
#import re
import bs4  # beautifulSoup4
from datetime import datetime
from selenium import webdriver
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

    # Remove once error handled or ending with .HTML fixed
    return pagecount

    currentDate = datetime.now()
    fileDate = datetime.fromtimestamp(os.path.getmtime("webcomic/" + filename))
    fileAge = currentDate - fileDate
    # print("Current Date: " + currentDate.strftime("%Y-%m-%d %H:%M:%S"))
    # print("File Date: " + fileDate.strftime("%Y-%m-%d %H:%M:%S"))
    # print(fileAge.days)

    # If file is less then a week old, don't update it.
    # Comic currently updates every Thursday
    if fileAge.days < 7:
        return pagecount

  # Current Latest page ends with '2476.html', need to handle error or make work
    try:
        driver = webdriver.Chrome()
        driver.get(urlMain)
        # select the next button
        latest_button = driver.find_element_by_xpath("//img[@src='latest.png']")
        latest_button.click()
        latestLink = driver.current_url
        driver.quit()
        latestPage = latestLink[-4:]
        pastLatest = str(int(latestPage) + 1).zfill(4)
    except TypeError:
        print("Chrome not found")
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
