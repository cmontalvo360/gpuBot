import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.bestbuy.com/site/lg-65-class-cx-series-oled-4k-uhd-smart-webos-tv/6401850.p?skuId=6401850")


element = driver.find_element_by_class_name("add-to-cart-button")
element.click()
time.sleep(3)
gotocartbtn = driver.find_element_by_class_name("go-to-cart-button")
gotocartbtn.click()

#deliverbtn = driver.find_element_by_class_name("availabilty__entry")
#deliverbtn.click()
time.sleep(3)
checkoutbtn = driver.find_element_by_class_name("checkout-buttons__checkout")
checkoutbtn.click()