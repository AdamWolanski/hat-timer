#!/usr/bin/python
import selenium
from selenium import webdriver
import getpass
import sys
import time
import re

import timer

#usage:
#  $ python scraper.py <args-optional>
#  args: 1(defalut) - count weekends, 0 - don't count

usr = getpass.getuser()
password = getpass.getpass()

browser = webdriver.Firefox()
time.sleep(2)
browser.get('hat.szczecin.tietoenator.com')
user_elem = browser.find_element_by_id('user_')
pass_elem = browser.find_element_by_id('pass_')

user_elem.send_keys(str(usr))

pass_elem.send_keys(str(password))

pass_elem.submit()

work_elem = browser.find_element_by_link_text('Work history')

work_elem.click()

tota_elem = browser.find_elements_by_class_name('m')

browser.close()

matchList = []

def regexParse(elems):    
    pattern = '([0-9].:..:..)'
    global matchList
    for element in tota_elem:
        x = re.search('([0-9].:..:..)', element.text)
        matchList.append(x.group(1))

def hatTimePrint(elems, args):
    if len(elems) == 5:
        if len(args) > 0:
            t = timer.timeCalculate(matchList[2], matchList[3], matchList[4], args[0])
        else:
            t = timer.timeCalculate(matchList[2], matchList[3], matchList[4])
        timer.timePrint(t)
    else:
        t = timer.timeCalculate(matchList[2], matchList[3])
        timer.timePrint(t)

def main(args):
    regexParse(tota_elem)
    hatTimePrint(matchList, args)

if __name__ == "__main__":
    main(sys.argv[1:])
