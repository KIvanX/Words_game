from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print('Loading...')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://rustxt.ru/dict')

input = driver.find_element(By.NAME, value='text')
input.clear()
input.send_keys('кот')
input.send_keys(Keys.ENTER)

if driver.find_elements(By.CLASS_NAME, value='alert'):
    print(driver.find_element(By.CLASS_NAME, value='alert').text)
else:
    table = driver.find_element(By.CLASS_NAME, value='font-weight-bold')
    print(table.text)

# words = []
# for el in list:
#     words.append(el.text[el.text.find(' ')+1:])
#
# with open('words.txt', 'w') as f:
#     f.write('\n'.join(words))

# with open('words.txt', 'r') as f:
#     words2 = f.read()
#
# print(words2.split('\n'))
#
# driver = webdriver.Firefox()
#
# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)