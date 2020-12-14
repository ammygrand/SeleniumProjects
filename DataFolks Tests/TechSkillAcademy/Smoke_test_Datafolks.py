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

# wait until the Submit button will be clickable, and click
submit_email_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
submit_email_btn.click()

# wait until text on the Pop-up window will be visible and verify its text
popup_window = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
(By.XPATH, "//div[contains(@class,'js-successbox t-form__successbox t-text t-text_md')]")))
assert popup_window.text == "Thank you! We will contact you soon."

# find close pup-up button and click
close_popup_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable(
(By.XPATH, "//div[contains(@class, 't-popup__close-wrapper')]")))
close_popup_btn.click()

#return to the home page
return_home = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/div[17]/div/div')))
return_home.click()

driver.quit()