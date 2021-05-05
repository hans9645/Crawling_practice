from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import webDriverWait
from selenium.webdriver.support import expected_condition as EC

#import time

#키값을 직접 입력가능
browser = webdriver.Chrome("./chromedriver")
browser.get("http://naver.com")
elem=browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")
browser.find_element_by_id("log.login").click()


# time.sleep(3)
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("as285")


print(browser.page_source)

#browser.quit()






# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()


# elem = browser.find_element_by_id("query")
# elem.send_keys("시가총액 순위")
# elem.send_keys(Keys.ENTER)


# elem = browser.find_elements_by_tag_name("a")
# for e in elem:
#     e.get_attribute("href")

# browser.get("http://daum.net")
# elem=browser.find_element_by_name("q")
# elem.send_keys("나도 코딩")
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")

# #elem.send_keys(Keys.ENTER)
# elem.click()

# browser.back()
