import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get('http://cnn.com')
print(driver.title)
try:
    menu = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "menuButton"))
    )
    menu.click()
except:
    print("fuck")
try:
    search = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "header-search-bar"))
    )
    search.send_keys("trump")
    search.send_keys(Keys.RETURN)
except:
    print("fuck")
while True:
    try:
        main = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "cnn-search__results")))
        nextButton = driver.find_element_by_class_name("pagination-arrow-right")
        nextButton.click()
    except:
        print("fuck")
    splitedMain = main.text.split(".")
    arr = []
    for sentence in splitedMain:
        splitedSentence = sentence.split()
        for word in splitedSentence:
            if word.lower() == 'trump':
                arr.append(sentence)
                f = open("trump1.txt", "a")
                f.write(sentence)
                f.close()
print("done")






