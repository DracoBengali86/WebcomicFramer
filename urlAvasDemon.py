import requests
import os
from datetime import datetime
from selenium import webdriver
from htmlCreator import buildComicPage

# latestPage = '2382'


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
                if lines[pagecount - 1] == "zzzENDzzz":
                    pagecount -= 1
                    url = lines[pagecount]
                else:
                    url = lines[pagecount - 1]

        currentDate = datetime.now()
        fileDate = datetime.fromtimestamp(os.path.getmtime("webcomic/" + filename))
        fileAge = currentDate - fileDate
        # print("Current Date: " + currentDate.strftime("%Y-%m-%d %H:%M:%S"))
        # print("File Date: " + fileDate.strftime("%Y-%m-%d %H:%M:%S"))
        # print(fileAge.days)

        # If file is less then a week old, don't update it.
        # Comic currently updates every Thursday
        if fileAge.days < 7 and not url.endswith('zzzENDzzz'):
            print("Latest search less then 7 days ago, rebuilding page (No search performed)")
            buildComicPage(pagecount, filename, True)
            return pagecount
            # If end of comic has been reached, don't search regardless
        elif url.endswith('zzzENDzzz'):
            print("End of Comic flag found, no search performed")
            buildComicPage(pagecount, filename, True)
            return pagecount

    try:
        driver = webdriver.Chrome()
        driver.get(urlMain)
        # select the next button
        latest_button = driver.find_element_by_xpath("//img[@src='latest.png']")
        latest_button.click()
        latestLink = driver.current_url
        driver.quit()
        latestPage = latestLink[-4:]
        if not latestPage.isdigit():
            lastDot = latestLink.rfind(".")
            latestPage = latestLink[lastDot - 4:lastDot]
            if not latestPage.isdigit():
                print("Failed to find Latest page")
                try:
                    buildComicPage(pagecount, filename, True)
                    return pagecount
                except:
                    print("building comic page failed!")
                    return 0
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

        # url = 'http://www.AvasDemon.com/pages.php?page=' + nextLink
        url = 'http://www.avasdemon.com/pages.php?page#' + nextLink

    pagecount = pagecount + i
    print('Done. Current Pagecount: ' + str(pagecount))

    # update modified date on file if latest page is last page in file
    if i == 0:
        try:
            os.utime("webcomic/" + filename)
        except:
            print("Error updating modified time: " + filename)
            exit(-1)

    buildComicPage(pagecount, filename, True)

    return pagecount


if __name__ == "__main__":
    comicname = "Ava's Demon"
    filename = "AvasDemon"
    urlMain = "http://www.AvasDemon.com"
    urlFirstPage = "http://www.AvasDemon.com/pages.php#0001"

    os.makedirs('webcomic', exist_ok=True)
    urlBuild(urlFirstPage, filename, urlMain)
