from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
sign_up_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-block')

first_name.send_keys("This is FName")
last_name.send_keys("This is LName")
email.send_keys("test@testapp.com")
sign_up_button.click()

driver.close()
