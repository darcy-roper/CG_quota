
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


#PATH = Service("Users/newmac/.wdm/drivers/chromedriver/mac64/99.0.4844.51/chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")

time.sleep(3)

