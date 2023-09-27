import time
from selenium import webdriver
#from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()

#driver.get("http://the-internet.herokuapp.com/basic_auth")
#driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.get("https://krank.com/")
driver.find_element(By.LINK_TEXT,"Explore Marketplace").click()
time.sleep(10)
#driver.find_element(By.CLASS_NAME,"sc-eeDRCY fnyekb")

#alertwindow.dismiss()

