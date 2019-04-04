import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://abhishekmadhu.com/South-Eastern-Railway-Ranchi-Internship-Portal/')

print(driver.title)


frame_irc = driver.find_element_by_tag_name('iframe')
print('Found')

try:

    driver.switch_to.frame(0)
    print('switched')

    input_box = driver.find_element_by_xpath('//*[@id="ircui"]/div[4]/table/tbody/tr/td/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/input')

    input_box.send_keys('nickname1')

    driver.switch_to.parent_frame()
    driver.maximize_window()

except Exception as e:
    print(e)
    print('failed')

finally:
    time.sleep(5)
    driver.quit()
