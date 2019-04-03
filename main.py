from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://mail.google.com/')


driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('uemcalcutta@gmail.com')

driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('idonotownaxolo')
driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()

time.sleep(5)

driver.close()
