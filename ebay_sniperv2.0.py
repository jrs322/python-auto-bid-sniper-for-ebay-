from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys
import re
MAX_BID = "your final bid with no dollar sign"
ITEM_URL = "Place url for item to purchase"
LOGIN_ID = "Id for login"
LOGIN_PASSWORD = "password for login"
time_left_unil_bid = 5


def connect_selenium_driver():
    try:
        driver = webdriver.Firefox()
        driver.get('https://www.ebay.com')
        time.sleep(3)
        return True
    except:
        print("The program did not make a connection")
        return False

def sign_in():
    io = driver.find_element_by_link_text('Sign in')
    io.click()
    time.sleep(3)
    elements = driver.find_elements_by_class_name("fld")
    elements[2].send_keys(LOGIN_ID)
    elements[3].send_keys(LOGIN_PASSWORD)
    button = driver.find_element_by_id("sgnBt")
    button.click()
    time.sleep(2)

def move_to_bid():
    print("Attempting Bid")
    driver.get(itemidurl)
    time.sleep(3)
    elements = driver.find_element_by_id("MaxBidId")
    elements.send_keys(maxbidebay)
    elements = driver.find_element_by_id("bidBtn_btn")
    elements.click()
    io = driver.find_element_by_css_selector("a[id*='reviewBidSec_btn']")
    io.click()
    time.sleep(20)
    driver.quit()

def main_loop():
    time_left_unil_bid = int(input("Enter time until bid - 15 sec Ex: 8.01 = 8 min 16 sec"))
    ITEM_URL = input("This is where you copy paste the url")
    LOGIN_PASSWORD = input("enter password")
    if len(LOGIN_PASSWORD) > 15:
        print ("Error! Only 15 characters allowed!")
        sys.exit()
    connected = connect_selenium_driver()
    if connected:
        loop = True
    else:
        loop = False
    time.sleep(time_left_unil_bid*60)
    sign_in()
    move_to_bid()

if __name__ == "__main__":
     main_loop()
