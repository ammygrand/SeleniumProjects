from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

home_button = driver.find_element_by_xpath("//div[@data-elem-id='1551634462374']/a") #code for home button
assert home_button.text == "Home"

portfolio_button = driver.find_element_by_xpath("//div[@data-elem-id='1551634481382']/a") #code for portfolio button
assert portfolio_button.text == "Portfolio"

services_button = driver.find_element_by_xpath("//div[@data-elem-id='1551634484712']/a")  # code for services button
assert services_button.text == "Services"

contact_us_button = driver.find_element_by_xpath("//div[@data-elem-id='1551634487768']/a") # code for Contact Us button
assert contact_us_button.text == "Contact Us"

driver.quit()