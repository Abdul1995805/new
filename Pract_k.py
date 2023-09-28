import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://krank.com/")
driver.find_element(By.LINK_TEXT,"Explore Marketplace").click()
time.sleep(5)

# Execute JavaScript and click the "Accept All" button
script = '''
    const shadowRoot = document.getElementById("usercentrics-root").shadowRoot;
    const acceptButton = shadowRoot.querySelector('button[data-testid="uc-accept-all-button"]');
    acceptButton.click();
'''
driver.execute_script(script)

time.sleep(3)

driver.find_element(By.CLASS_NAME, "close-btn").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT,"2007 HAMM GRW 15").click()
time.sleep(2)

#NEED TO CLICK ON SEND ENQUIREY BUTTON 




#driver.find_element(By.ID,"enq_full_name").send_keys("Abdul")
#driver.find_element(By.ID,"enq_company").send_keys("ABSOFT")
#driver.find_element(By.ID,"enq_email").send_keys("Abdul@yopmail.com")
#driver.find_element(By.ID,"enq_phone").send_keys("585858222258")
#driver.find_element(By.ID,"enq_message").send_keys("test text")



#alertwindow.dismiss()
driver.quit()
