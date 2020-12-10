from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r'C:\Users\sergiu\PycharmProjects\TechSkillAcademy\geckodriver.exe')
driver.get("https://www.datafolks.com")

contact_us_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-elem-id=1551726675405]/a')))
assert contact_us_btn.text == "CONTACT US"

# wait until Contact Us in Navigation bar is clickable
contact_us_navigation_bar_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Contact Us')]")))
contact_us_navigation_bar_btn.click()

# wait until logo on the contact page is visible and verify its text
logo_on_the_contact_page = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.CLASS_NAME,"tn-atom")))
assert logo_on_the_contact_page.text == "DATAFOLKS"

# wait until text on Contact Us page is visible and verify its text
contact_page_header = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
(By.XPATH, '//div[@data-elem-id=1551634856822]/h1')))
assert contact_page_header.text == "Get in touch"

# wait until email input field is visible and input mail@example.com
email_input_field = WebDriverWait(driver,20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("mail@example.com")

# wait until Submit button is clickable and click on it
submit_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div/div[1]/div/div/div[10]/div[1]/form/div[2]/div[3]/button')))
submit_btn.click()

# wait until Thank you popup is visible and verify its text
pop_up = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.ID, 'tildaformsuccesspopuptext')))
assert pop_up.text == "Thank you! We will contact you soon."

# find close popup button and click
close_popup = WebDriverWait(driver,20).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[2]/div/div/svg[1]')))
close_popup.click()

#come back on the home page
home_page = WebDriverWait(driver,20).until(EC.element_to_be_clickable(
    (By.XPATH, '//div[@data-elem-id=1551634462374]/a')))
home_page.click()

driver.quit()