import selenium
from selenium import webdriver
import getpass
import sys
import time

usr = getpass.getuser()
passs = getpass.getpass()


browser = webdriver.Firefox()
time.sleep(0.5)
browser.get('hat.szczecin.tietoenator.com')
user_elem = browser.find_element_by_id('user_')
pass_elem = browser.find_element_by_id('pass_')

user_elem.send_keys(str(usr))

pass_elem.send_keys(str(passs))

pass_elem.submit()

work_elem = browser.find_element_by_link_text('Work history')

work_elem.click()

tota_elem = browser.find_elements_by_class_name('m')

browser.close()

print tota_elem[0].text
print tota_elem[1].text
print tota_elem[2].text
print tota_elem[3].text