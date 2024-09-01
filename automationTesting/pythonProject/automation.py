from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://zapier.com/blog/github-delete-repository/')
#
# assert 'How to delete a repository in' in browser.title
#
# my_element = browser.find_element(By.CLASS_NAME, "css-1ilpmu8")
# print(my_element.get_attribute('innerHTML'))
#
# my_element1 = browser.find_elements(By.CLASS_NAME, 'css-g52fnz-BaseButton__buttonText')
# print(my_element1[2].get_attribute('innerHTML'))

# my_element2 = browser.find_element(By.CSS_SELECTOR, '#APjFqb')
# my_element3 = browser.find_element(By.CSS_SELECTOR, '#SDkEP')
# my_element2.clear()
# my_element2.send_keys("hey")
# my_element2.click()
# print(my_element3)

my_element4 = browser.find_elements(By.CSS_SELECTOR, '.ee1bhfr4')
my_element5 = browser.find_element(By.CSS_SELECTOR, ".css-g52fnz-BaseButton__buttonText")
my_element6 = browser.find_element(By.CSS_SELECTOR, ".css-18t6a9j-Input__input-TextInput__input--fullwidth")
print(my_element4[1].get_attribute('innerHTML'))
print(my_element5.click())
print(my_element6)

# my_element4[1].click()
