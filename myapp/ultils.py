from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time 

def autoLike():
    driver = webdriver.Firefox(executable_path=r'D:\Study\Python\Django\geckodriver.exe')
    driver.get("http://www.facebook.com")
    cookies = pickle.load(open('D:\Study\Python\Django\webbanhang\myapp\cookie.pkl','rb'))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("http://www.facebook.com")