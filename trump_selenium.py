from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def page_is_loading(driver):
    while True:
        x = driver.execute_script("return document.readyState")
        if x == "complete":
            return True
        else:
            yield False



def find_trump():
    PATH = 'C:\Program Files (x86)\chromedriver.exe'

    pages = np.arange(0, 100220, 10)

    driver = webdriver.Chrome(PATH)
    i = 0
    for page in pages:
        i = i + 1
        try:
            driver.get(f'https://edition.cnn.com/search?q=trump&size={10}&from={page}&page={i}')
            print(driver.title)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "cnn-search__results-list")))
            while not page_is_loading(driver):
                continue
            sleep(2)
            links = driver.find_elements_by_class_name("cnn-search__result-contents")
            for z in range(0, len(links)):
                try:
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "cnn-search__result-thumbnail")))
                    driver.implicitly_wait(60)
                    links2 = driver.find_elements_by_class_name("cnn-search__result-thumbnail")
                    driver.implicitly_wait(60)
                    links2[z].click()
                    while not page_is_loading(driver):
                        continue
                    sleep(2)
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.TAG_NAME, "body")))
                except Exception as e:
                    print("click error:", e)
                sleep(2)
                page_source = driver.page_source
                cleaned_page = cleanhtml(page_source)
                split_source = cleaned_page.split(".")
                for sentence in split_source:
                    split_sentence = sentence.split()
                    for word in split_sentence:
                        if word.lower() == 'trump':
                            try:
                                f = open("trump.txt", "a")
                                sentence_to_write = " ".join(split_sentence)
                                f.write(sentence_to_write + "\n")
                                f.close()
                            except:
                                print("problem2")
                driver.get(f'https://edition.cnn.com/search?q=trump&size={10}&from={page}&page={i}')
                while not page_is_loading(driver):
                    continue

        except Exception as e:
            print(e)
            driver.quit()


if __name__ == '__main__':
    find_trump()
