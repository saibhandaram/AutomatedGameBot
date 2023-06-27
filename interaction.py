from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver instance
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()  # Make sure you have geckodriver installed and in the PATH

driver.get("https://en.wikipedia.org/wiki/Main_Page")

div_article_count = driver.find_element(By.ID,"articlecount")
article_count = div_article_count.find_element(By.TAG_NAME,'a').text

print(article_count)

# Close the browser
driver.close()