from selenium import webdriver
import time

browser = webdriver.Chrome('C:\\Users\\오정인\\Desktop\\chromedriver_win32\\chromedriver')

browser.get("http://python.org")

menus = browser.find_element_by_css_selector('#top > nav > ul > li.pypi-meta > a')

pypi = menus

pypi.click()

time.sleep(5)
browser.quit()