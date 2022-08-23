from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import time
import binascii

FIRST_NAME = 'woman'
LAST_NAME = '1'
USERNAME = str(binascii.hexlify(b'sdfe-1'))[2:-1]
PASSWORD = str(binascii.hexlify(b'password_sdfe-1'))[2:-1]


def waitForLoad(xpath):
	wait = WebDriverWait(driver, 500)
	wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)


url = "https://accounts.google.com/signin"
driver.get(url)

temp = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button'
waitForLoad(temp)
driver.find_element(By.XPATH, temp).click()
temp = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]'
waitForLoad(temp)
driver.find_element(By.XPATH, temp).click()

temp = '//*[@id="firstName"]'
waitForLoad(temp)
driver.find_element(By.XPATH, temp).send_keys(FIRST_NAME)
temp = '//*[@id="lastName"]'
driver.find_element(By.XPATH, temp).send_keys(LAST_NAME)
temp = '//*[@id="username"]'
driver.find_element(By.XPATH, temp).send_keys(USERNAME)
temp = '//*[@id="passwd"]/div[1]/div/div[1]/input'
driver.find_element(By.XPATH, temp).send_keys(PASSWORD)
temp = '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'
driver.find_element(By.XPATH, temp).send_keys(PASSWORD)
temp = '//*[@id="accountDetailsNext"]/div/button'
driver.find_element(By.XPATH, temp).click()
# time.sleep(5)
# driver.quit()