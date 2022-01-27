from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://rustxt.ru/dict')


def check(word):
    input = driver.find_element(By.NAME, value='text')
    input.clear()
    input.send_keys(word)
    input.send_keys(Keys.ENTER)

    if driver.find_elements(By.CLASS_NAME, value='alert'):
        return -1

    output = driver.find_element(By.CLASS_NAME, value='font-weight-bold').text.lower()
    for teg in ['единственное число', 'именительный падеж']:
        if teg not in output:
            return 0
    for teg in ['прилагательное', 'наречие', 'лицо']:
        if teg in output:
            return 0

    return 1
