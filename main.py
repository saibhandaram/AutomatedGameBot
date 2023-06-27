from selenium import webdriver

# Set up the WebDriver instance
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()  # Make sure you have geckodriver installed and in the PATH

# Navigate to a website
driver.get("https://www.python.org/")

# find elements


search_bar = driver.find_element(By.ID, 'id-search-field')
# print(search_bar.get_attribute("Placeholder"))

ul_list_upcoming_events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

li__list_upcoming_events = ul_list_upcoming_events.find_elements(By.TAG_NAME, "li")
my_dict = {}
i = 0
for item in li__list_upcoming_events:
    my_dict[i] = {
        "time": item.find_element(By.TAG_NAME, "time").text,
        "name": item.find_element(By.TAG_NAME, "a").text
    }

    i += 1

print(my_dict)

# Close the browser
driver.close()
