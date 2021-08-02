import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from htmlCreator import buildComicPage

# latestPage = '2382'


def urlBuild(urlFirstPage, filename, urlMain, urlVol1End, urlVol2):
    url = urlFirstPage
    writeURL = True
    pagecount = 0
    prevLink = ""
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

        # If file is less then a week old, don't update it.
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
        driver.get(url)
        delay = 240  # seconds
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'btnNext')))
        except TimeoutException:
            print("Failed to load page")
            try:
                buildComicPage(pagecount, filename, True)
                return pagecount
            except Exception as err:
                print("building comic page failed!")
                print("Error:", err)
                return 0

        while prevLink != url:
            print('Finding page %s...' % url)

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

            prevLink = url

            if url == urlVol1End:
                url = urlVol2
                driver.get(url)
            else:
                # select the next button
                next_button = driver.find_element_by_xpath("//img[@id='btnNext']")
                next_button.click()
                url = driver.current_url
                time.sleep(0.5)
                while prevLink == url:
                    for j in range(5):
                        print("Waiting for page load (" + str(5-j) + ")")
                        time.sleep(1)
                    break

        pagecount = pagecount + i
        print('Done. Current Pagecount: ' + str(pagecount))

        driver.quit()

    except TypeError:
        print("Chrome not found")
        print("***Blade Bunny is currently broken***")
        print('***Current Pagecount: ' + str(pagecount) + '***\n')
        try:
            buildComicPage(pagecount, filename, True)
        except Exception as err:
            print("building comic page failed!")
            print("Error:", err)
            return 0
        return pagecount

    # update modified date on file if latest page is last page in file
    if i == 0:
        try:
            os.utime("webcomic/" + filename)
        except Exception as err:
            print("Error updating modified time: " + filename)
            print("Error:", err)
            exit(-1)

    buildComicPage(pagecount, filename, True)

    return pagecount


if __name__ == "__main__":
    comicname = "Blade Bunny"
    filename = "BladeBunny"
    urlMain = "https://readcomiconline.to/Comic/Blade-Bunny"
    urlFirstPage = "https://readcomiconline.to/Comic/Blade-Bunny/Issue-5?id=87724#27"
    urlVol1End = "https://readcomiconline.to/Comic/Blade-Bunny/Issue-5?id=87724#29"
    urlVol2 = "https://readcomiconline.to/Comic/Blade-Bunny-Vol-2/Issue-1?id=94715"

    os.makedirs('webcomic', exist_ok=True)
    urlBuild(urlFirstPage, filename, urlMain, urlVol1End, urlVol2)
