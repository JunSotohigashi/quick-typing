import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(executable_path='./msedgedriver.exe')
driver.get('https://manabi-gakushu.benesse.ne.jp/gakushu/typing/nihongonyuryoku.html')
driver.find_element(By.ID, "goSettingButton").click()
#time.sleep(1)
driver.find_element(By.CLASS_NAME, "typingButton").click()
#time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SPACE)

while  driver.find_element(By.ID, "remainingTimeMinutes").text != "0" or driver.find_element(By.ID, "remainingTimeSeconds").text != "00":
    driver.find_element(By.TAG_NAME, "body").send_keys(driver.find_element(By.ID, "remaining").text)

print("Finished")
time.sleep(10)
driver.quit()