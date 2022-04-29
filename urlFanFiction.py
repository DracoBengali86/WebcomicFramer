import os
from datetime import datetime
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from htmlCreator import buildComicPage


def urlBuild(url_first_page, file_name):
    url = url_first_page
    write_url = True
    page_count = 0
    i = 0

    if os.path.isfile(os.path.join('webcomic', file_name)):
        file_exists = True
    else:
        file_exists = False

    if file_exists:
        with open(os.path.join('webcomic', file_name), 'r') as f:
            lines = f.read().splitlines()
            page_count = len(lines)
            if page_count > 0:
                write_url = False
                if lines[page_count - 1] == "zzzENDzzz":
                    page_count -= 1
                    url = lines[page_count]
                else:
                    url = lines[page_count - 1]
        current_date = datetime.now()
        file_date = datetime.fromtimestamp(os.path.getmtime("webcomic/" + file_name))
        file_age = current_date - file_date

        # If file is less than a week old, don't update it.
        if file_age.days < 30 and not url.endswith('zzzENDzzz'):
            print("Latest search less then 30 days ago, rebuilding page (No search performed)")
            buildComicPage(page_count, file_name)
            return page_count
        # If end of comic has been reached, don't search regardless
        elif url.endswith('zzzENDzzz'):
            print("End of Comic flag found, no search performed")
            buildComicPage(page_count, file_name)
            return page_count

    if not url.endswith('zzzENDzzz'):
        try:
            driver = uc.Chrome(use_subprocess=True)
            driver.get(url)
        except TimeoutException as err1:
            print("WebDriver Timeout")
            print(" *** ")
            print(err1)
            print(" *** ")
            buildComicPage(page_count, file_name)
            return page_count
        except WebDriverException as err2:
            print("WebDriver Exception")
            print(" *** ")
            print(err2)
            print(" *** ")
            buildComicPage(page_count, file_name)
            return page_count

    # Stop if the next url is the "search_end", or no next URL is found, or next URL is the same as the previous URL
    while not url.endswith('zzzENDzzz'):
        # Download page
        print('Finding page %s...' % url)

        if write_url:
            try:
                comic_file = open(os.path.join('webcomic', file_name), "a")
                comic_file.write(url + "\n")
                comic_file.close()
            except IOError:
                print("Error opening comic file: " + file_name)
                exit(-1)

            i += 1
        else:
            write_url = True

        # Find and click the next button
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()=' Follow/Favorite']"))
            )
        except TimeoutException as err3:
            print(" *** ")
            print(err3)
            print(" *** ")
            print("Page failed to load")
            break

        try:
            next_button = driver.find_element(By.XPATH, "//button[text()='Next >']")
        except NoSuchElementException:
            print("next link couldn't be found")
            print("last found page: " + url)
            break
        next_button.click()
        url = driver.current_url

    page_count = page_count + i
    print('Done. Current Page Count: ' + str(page_count))

    # update modified date on file if latest page is last page in file
    if i == 0:
        try:
            os.utime("webcomic/" + file_name)
        except Exception as err:
            print("Error updating modified time: " + file_name)
            print("Error:", err)
            exit(-1)

    buildComicPage(page_count, file_name)

    return page_count


if __name__ == "__main__":
    comic_name = "zFF Four Armed Bride"
    filename = "zfourarmedtest"
    urlFirstPage = "https://www.fanfiction.net/s/12103554/1/Four-Armed-Bride"

    os.makedirs('webcomic', exist_ok=True)
    urlBuild(urlFirstPage, filename)
