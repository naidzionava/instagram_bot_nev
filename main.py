from auth import login, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random

browser = None


def login_firefox_chrome(_browser, login, password):
    global browser
    if _browser == "Chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com')
    time.sleep(random.randrange(1, 2))

    _login = browser.find_element(By.NAME, "username")
    _login.clear()
    _login.send_keys(login)

    time.sleep(random.randrange(1, 2))

    _password = browser.find_element(By.NAME, "password")
    _password.clear()
    _password.send_keys(password)

    time.sleep(random.randrange(1, 2))

    _password.send_keys(Keys.ENTER)

    # _login_button = browser.find_element_by_css_selector('button[type="submit"]')
    # _login_button.click()


def close_browser():
    global browser
    browser.close()
    browser.quit()


def search_by_hashtag(hashtag):
    global browser
    browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

    for i in range(1,4):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randrange(2, 5))

    hrefs = browser.find_elements(By.TAG_NAME, "o")
    urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
    print(urls)

    for url in urls:
        browser.get(url)
        like = browser.find_elements(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[1]/button/div[1]/svg")
        like.click()
        time.sleep(10000)

    # for item in hrefs:
    #     href = item.get_attribute('href')
    #     if "/p/" in href:
    #         urls.append(href)
    #         print(href)


login_firefox_chrome("Chrome", login, password)
time.sleep(5)
search_by_hashtag("rose")
time.sleep(200)
close_browser()
