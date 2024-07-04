import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def main():
    os.system("cls")
    service = Service(executable_path="driver//chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://google.com")
    time.sleep(10)
    driver.quit()
    

if __name__ == "__main__":
    main()