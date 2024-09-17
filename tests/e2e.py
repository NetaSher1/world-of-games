import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
url = "http://127.0.0.1:5000"

def test_scores_service(url):
    check_file = os.path.isfile("../webGames/score.txt")
    if not check_file:
        return False
    else:
        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element(By.ID, "user_name").send_keys("testBot")
        driver.find_element(By.ID, "submit-button").click()
        driver.find_element(By.ID, "scoreBtn").click()
        results = driver.find_elements(By.ID,"score")
        results = set([int(e.text.split(":",1)[1]) for e in results])
        for i in results:
            if not 20 < i < 1000:
                return False
            else:
                return True

def main():
    if test_scores_service(url):
        return sys.exit(0)
    else:
        return sys.exit(-1)
main()