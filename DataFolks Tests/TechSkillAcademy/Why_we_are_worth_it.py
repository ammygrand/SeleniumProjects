from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r'C:\Users\sergiu\PycharmProjects\TechSkillAcademy\geckodriver.exe')
driver.get("https://www.datafolks.com")

worth_it_btn = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/div[1]/div/div/div[11]/a/u')))
worth_it_btn.click()

mobile_dev = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.XPATH, '//div[@data-elem-id=1551735998271]/div')))
assert mobile_dev.text == "Mobile Development"


web_dev = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/div[6]/div/div/div[5]/div')))
assert web_dev.text == "Web Development"

aug_real = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.XPATH, '//div[@data-elem-id=1551735997222]/div')))
assert aug_real.text == "Augmented Reality"

virtual_real = WebDriverWait(driver,20).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div/div[6]/div/div/div[4]/div')))
assert virtual_real.text == "Virtual Reality"

driver.quit()
