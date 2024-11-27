# import time
#
from selenium import webdriver
# from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/login/")                 #Open an URL
time.sleep(2)                                                 #Dwell Time
import time

print(driver.title)                                         #Page Title
print(driver.current_url)                                   #Page URL
driver.back()                                               #Navigation
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)

#########______X-Path_______
# //*[@id="email"]

# //tagname[@id="attribute Value"]          #Formula

driver.find_element(By.XPATH, '//input[@id="email"]').send_keys("Swapnil Dixit")
time.sleep(2)

driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys("Hello")
time.sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT,"Sign up for Facebook").click()
time.sleep(5)

driver.save_screenshot("skd.png")




#########____-iFrames_____########


from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://www.facebook.com/login/")
time.sleep(3)
#
# driver.back()
# time.sleep(3)
#
# driver.forward()
# time.sleep(3)
#
# driver.refresh()
# time.sleep(3)
#
# driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("SKD_Hero")
# time.sleep(3)
#
# driver.find_element(By.XPATH,'//*[@id="login_link"]/a[2]').click()
# time.sleep(2)
#
# driver.find_element(By.PARTIAL_LINK_TEXT,'Already have an account?').click()
# time.sleep(3)

print("The Current URL=", driver.current_url)
print("The title of the URL is",driver.title)
driver.quit()
