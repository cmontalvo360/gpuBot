#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.bestbuy.com/site/lenovo-chromebook-duet-10-1-tablet-128gb-with-keyboard-ice-blue-iron-gray/6401727.p?skuId=6401727")

def main():
    buyItem()

def buyItem():
    # finds add to cart button and clicks it
    element = driver.find_element_by_class_name("add-to-cart-button")
    element.click()
    
    # finds go to cart button and clicks it
    gotocartbtn = driver.find_element_by_class_name("go-to-cart-button")
    gotocartbtn.click()

    #deliverbtn = driver.find_element_by_class_name("availabilty__entry")
    #deliverbtn.click()

    # finds go to cart button and clicks it
    checkoutbtn = driver.find_element_by_class_name("checkout-buttons__checkout")
    checkoutbtn.click()
    
    # continue checking out as guest 
    guestbtn = driver.find_element_by_class_name("guest")
    guestbtn.click()
    
    #fills in contact info
    email = driver.find_element_by_id("user.emailAddress")
    email.send_keys("cmontalvo360@yahoo.com")
    phonenum = driver.find_element_by_id("user.phone")
    phonenum.send_keys("2532927776")

    # continue to payment screen
    contbtn = driver.find_element_by_class_name("button--continue")
    contbtn.click()

    # fill in payment options
    creditcard = driver.find_element_by_xpath("//*[@id='optimized-cc-card-number']")
    creditcard.send_keys("2424887613140099")

    #billing info
    fname = driver.find_element_by_id("payment.billingAddress.firstName")
    fname.send_keys("Joe")
    lname = driver.find_element_by_id("payment.billingAddress.lastName")
    lname.send_keys("Smoe")
    addr_toggle = driver.find_element_by_class_name("autocomplete__toggle")
    addr_toggle.click()
    address = driver.find_element_by_id("payment.billingAddress.street")
    address.send_keys("11223 72nd Avenue Ct E")
    city = driver.find_element_by_id("payment.billingAddress.city")
    city.send_keys("tacoma")
    state = Select(driver.find_element_by_id("payment.billingAddress.state"))
    state.select_by_value("WA")
    zipcode = driver.find_element_by_id("payment.billingAddress.zipcode")
    zipcode.send_keys("98444")

    #place order
    orderbtn = driver.find_element_by_class_name("payment__order-summary")
    orderbtn.click()

if __name__ == "__main__":
    main()