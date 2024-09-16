import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

form_url = ("https://docs.google.com/forms/d/e/1FAIpQLSe2wgE_qJmdp5hbF8iOs2GgwC5YFG2hecN7vklmNUcFHsWf5g/viewform?usp"
            "=sf_link")

zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(zillow_clone_url)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
list_of_links = [item.a.get("href") for item in soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")]
print(list_of_links)
list_of_price = [item.span.getText() for item in soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")]
prices = []
for price in list_of_price:
    if "+" in price:
        prices.append(price.split("+")[0])
    else:
        prices.append(price.split("/")[0])

print(prices)
list_of_addresses = [item.address.getText().strip() for item in soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")]
print(list_of_addresses)

driver = webdriver.Chrome()
driver.get(form_url)
for i in range(len(prices)-1):
    time.sleep(5)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_per_month = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_to_property = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address_input.send_keys(list_of_addresses[i])
    price_per_month.send_keys(prices[i])
    link_to_property.send_keys(list_of_links[i])
    submit_button.click()
    time.sleep(2)
    another_submission = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_submission.click()


