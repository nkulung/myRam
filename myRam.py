import requests
import urllib3
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys


def getEmailLogin():
    f = open('login_credentials.text','w+')
    smtp = input('Enter smtp address: ')
    email = input('Enter email: ')
    password = input('Enter email password: ')
    
    
    

def getLoginPage():

    driver = webdriver.Firefox()
    driver.get("https://get.cbord.com/portal/full/portal.php")
    html = driver.page_source

    soup = bs(html,"html.parser")
    token = soup.find("input", {"name" : "formToken"}).attrs
    tokenValue = token['value']
    print(tokenValue)
    options = driver.find_element_by_id('select_institution')
    for option in options.find_elements_by_tag_name('option'):
        if option.text == 'University of Rhode Island':
            option.click()
            break
    driver.find_element_by_id('submit').click()
    return driver

def selectSchool(driver):
    un = driver.find_element_by_id('login_username_text')
    pw = driver.find_element_by_id('login_password_text')

    unText = un.get_attribute('placeholder')
    pwText = pw.get_attribute('placeholder')

    print('Please enter the following information: ')
    username = input(unText + ': ')
    password = input(pwText + ': ')

    un.send_keys(username)
    pw.send_keys(password)
    driver.find_element_by_id('login_submit').click()
    
def sendInfo(driver):
    

def main():
    driver = getLoginPage()
    selectSchool(driver)






#payload = {'select_institution': 'uri', 'formToken': tokenValue}
#url = driver.current_url
#r = requests.post(url, data=payload)
#driver.find_element_by_id("formToken").sendKeys(tokenValue)
#driver.find_element_by_id("select_institution").sendKeys('uri')



#driver.sendKeys('uri')
#driver.sendKeys(tokenValue)
#school.sendKeys('uri')
#formToken.sendKeys(tokenValue)






