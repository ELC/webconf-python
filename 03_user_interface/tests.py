import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


global_delay = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:5000/")


# Test Title

time.sleep(global_delay)

title = driver.find_elements_by_xpath("//h1")[0].text

assert "Task Tracker" in title, "####### Title Displayed: FAIL #######"
print("####### Title Displayed: PASS #######")


# Test Initial Cards - GET

time.sleep(global_delay)

initial_tasks = {"Doctors Appointment", "Meeting at School"}

cards_titles = driver.find_elements_by_xpath("//h3")
cards_titles_text = {card_title.text for card_title in cards_titles}

assert initial_tasks == cards_titles_text, "####### Initial Cards loaded: FAIL #######"
print("####### Initial Cards loaded: PASS #######")

# Test adding cards - INSERT

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

add_button = driver.find_elements_by_xpath('//*[@id="app"]/div/header/button')[0]
add_button.click()

task_name = driver.find_elements_by_xpath('//*[@id="app"]/div/form/div[1]/input')[0]
task_name.send_keys("Testing Task")

task_date = driver.find_elements_by_xpath('//*[@id="app"]/div/form/div[2]/input')[0]
task_date.send_keys("Tomorrow Morning")
task_date.send_keys(Keys.ENTER)
driver.get("http://localhost:5000/")

delay = 5
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//h3')))

cards_titles = driver.find_elements_by_xpath("//h3")
cards_titles_text = {card_title.text for card_title in cards_titles}

new_cards = initial_tasks.union({"Testing Task"})

assert new_cards == cards_titles_text, "####### Add Card: FAIL #######"
print("####### Add Card: PASS #######")


# Test removing a card - DELETE

time.sleep(global_delay)

delete_icon = driver.find_elements_by_xpath('/html/body/div/div/div[3]/div/h3/i')[0]
delete_icon.click()

time.sleep(0.5)

cards_titles = driver.find_elements_by_xpath("//h3")
cards_titles_text = {card_title.text for card_title in cards_titles}

assert initial_tasks == cards_titles_text, "####### Delete Card: FAIL #######"
print("####### Delete Card: PASS #######")

driver.close()
