from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.google.com')
print(browser.title)

elem = browser.find_element_by_name('q') # Find the search box
elem.send_keys('firebug' + Keys.RETURN)

#browser.quit()
