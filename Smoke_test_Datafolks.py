from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r'C:\Users\sergiu\PycharmProjects\TechSkillAcademy\geckodriver.exe')
driver.get("https://www.datafolks.com")

#verify Contact Us button text
contact_us_popup = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.XPATH, '//div[@data-elem-id=1551726675405]/a')))
assert contact_us_popup.text == "CONTACT US"

# click on Contact Us button
contact_us_popup = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.XPATH, '//div[@data-elem-id=1551726675405]/a')))
contact_us_popup.click()

# fill out name field of Contact Us form
contact_us_name = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.NAME, "Name")))
contact_us_name.send_keys("John")

# fill out email field of Contact Us form
contact_us_email = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.NAME, "Email")))
contact_us_email.send_keys("John@example.com")

# fill out phone field of Contact Us form
contact_us_phone = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.NAME, "Phone")))
contact_us_phone.send_keys("+123 456 7890")

# fill out country field of Contact Us form
contact_us_country = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.NAME, "Country")))
contact_us_country.send_keys("USA")

# click on send button
contact_send_btn = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
(By.XPATH, '/html/body/div/div[17]/div/div/div[2]/div/form/div[2]/div[6]/button')))
contact_send_btn.click()

#close popup window
close_popup = WebDriverWait(driver,30).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/div[17]/div/div/div[1]/div')))
close_popup.click()

#return to the home page
return_home = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/div[17]/div/div')))
return_home.click()

driver.quit()
