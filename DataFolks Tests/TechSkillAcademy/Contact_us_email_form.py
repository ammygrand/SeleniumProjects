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
    (By.XPATH, "//button[@type='submit']")))
submit_btn.click()

# wait until text on the Pop-up window will be visible and verify its text
popup_window = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
(By.XPATH, "//div[@id='tildaformsuccesspopuptext']/div")))
assert popup_window.text == "Thank you! We will contact you soon."

# find close popup button and click
close_popup = WebDriverWait(driver,30).until(EC.element_to_be_clickable(
    (By.XPATH, "//path[contains(@d, 'M0 1.41L1.4 0l21.22 21.21-1.41 1.42z')]")))
close_popup.click()

#come back on the home page
home_page = WebDriverWait(driver,20).until(EC.element_to_be_clickable(
    (By.XPATH, '//div[@data-elem-id=1551634434793]/a')))
home_page.click()

driver.quit()