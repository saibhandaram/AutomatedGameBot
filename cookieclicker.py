from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")


def print_help():
    # Print Money
    money_val = driver.find_element(By.ID, 'money').text
    if "," in money_val:
        money_val = money_val.replace(",", "")
    print(f"Money : {money_val}")

    div_elements = driver.find_elements(By.CSS_SELECTOR, "div[onclick*='Buy'][class='']")
    name = []
    value_list = []
    for item in div_elements:
        print(f"--------------------------")
        name.append(item.find_element(By.TAG_NAME, 'b').text.split("-")[0].strip())
        value_list.append(item.find_element(By.TAG_NAME, 'b').text.split("-")[1].strip().replace(",", ""))

    new_list = [int(item) for item in value_list]
    # Find the index of the maximum value
    max_index = new_list.index(max(new_list))
    print(f"names :{name} and values :{new_list}")

    print(f"Index is {max_index} and max is {max(new_list)}")
    print(f"value to print {name[max_index]}")
    click_text = f"buy{name[max_index]}"
    print(click_text)
    driver.find_element(By.XPATH, f"//*[@id='{click_text}']").click()


def max_item_from_store(c_money):
    money = c_money
    store_item = driver.find_element(By.ID, 'store')
    store_items = store_item.find_elements(By.TAG_NAME, 'b')
    my_dict = {}
    # for item in store_items:
    #     my_dict = {
    #     'name' : item.text.split("-")[0].strip(),
    #     'value' : item.text.split("-")[1].strip()
    #     }

    print(my_dict)


start_time = time.time()
timeout = time.time() + 60 * 5

while time.time() < timeout:
    cookie.click()
    current_time = time.time()
    if ((int(current_time) - int(start_time)) > 20):
        print_help()
        start_time = current_time

time.sleep(5)

driver.quit()
