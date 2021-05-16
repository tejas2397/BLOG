from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import urllib.request
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install())
driver.get('https://www.google.com/')
search = driver.find_element_by_name('q')
search.send_keys('people wearing mask',Keys.ENTER)

elem = driver.find_element_by_link_text('Images')
elem.get_attribute('href')
elem.click()
value = 0
for i in range(10):
	driver.execute_script('scrollBy("+ str(value) +",+500);')
	value += 100
	time.sleep(4)
elements = driver.find_elements_by_xpath('//img[contains(@class,"rg_i")]')
count = 0
for i in elements:
    src = i.get_attribute('src')
    try:
        if src != None:
            src  = str(src)
            count+=1
            urllib.request.urlretrieve(src, os.path.join('images/with_mask','with_mask_image'+str(count)+'.jpg'))
            if count%10 == 0: print("downloaded",count,"images")
        else:
            raise TypeError
    except TypeError:
        pass


