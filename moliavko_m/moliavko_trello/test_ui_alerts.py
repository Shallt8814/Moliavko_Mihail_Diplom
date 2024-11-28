import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

with allure.step("проверка первого алерта"):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "alertButton"))
    )
    button.click()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert alert.text == "You clicked a button"
    alert.accept()

with allure.step("проверка второго алерта"):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "timerAlertButton"))
    )
    button.click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    time.sleep(5)
    alert.accept()

with allure.step("проверка третьего алерта"):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "confirmButton"))
    )
    button.click()
    confirm = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert confirm.text == "Do you confirm action?"
    confirm.dismiss()
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.ID, "promtButton"))
    button.click()

with allure.step("проверка четвертого алерта"):









    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.ID, "promtButton"))
    button.click()
    prompt = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert prompt.text == "Please enter your name"
    prompt.send_keys("Test User")
    prompt.accept()
    prompt_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.ID, "promptResult"))
    assert prompt_text.text == "You entered: Test User"

driver.quit()





