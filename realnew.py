from selenium import webdriver

path = "C:\\Users\\오정인\\Desktop\\chromedriver_win32\\chromedriver"
driver = webdriver.Chrome(path)

driver.get('https://www.naver.com')
search_box = driver.find_element_by_name('query')
search_box.send_keys("빅뱅")
search_box.submit()