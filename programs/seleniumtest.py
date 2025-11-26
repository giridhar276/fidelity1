



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://demoqa.com/automation-practice-form"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    driver.get(URL)
    driver.maximize_window()

    # Fill text fields
    wait.until(EC.element_to_be_clickable((By.ID, "firstName"))).send_keys("Giridhar")
    time.sleep(5)
    driver.find_element(By.ID, "lastName").send_keys("Sripathi")
    time.sleep(5)
    driver.find_element(By.ID, "userEmail").send_keys("giridhar@example.com")

    # Gender radio (input is hidden; click the label)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-1']"))).click()  # Male
    # gender radio ids exist like gender-radio-1 :contentReference[oaicite:1]{index=1}
    time.sleep(5)
    # Mobile number
    driver.find_element(By.ID, "userNumber").send_keys("9876543210")
    time.sleep(5)

    # Submit
    submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    driver.execute_script("arguments[0].click();", submit_btn)

    # Verify success modal
    wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    print("Form submitted successfully!")

finally:
    driver.quit()

