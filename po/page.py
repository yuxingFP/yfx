from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.common.exceptions import TimeoutException
from time import sleep

class Page():
        def __init__(self,driver):
            self.driver = driver
        def open(self,url):
            self.driver.get(url)
            self.driver.maximize_window()
        def find_element(self,*loc):
            try:
                sleep(1)
                wait = Wait(self.driver, timeout=10)
                wait.until(lambda x:x.find_element(*loc).is_displayed())
                return self.driver.find_element(*loc)
            except TimeoutException:
                print("超时异常")

        def find_elements(self,*loc):
            try:
                sleep(1)
                wait = Wait(self.driver, timeout=10)
                wait.until(lambda x: x.find_elements(*loc).is_displayed())
                return self.driver.find_elements(*loc)
            except TimeoutException:
                print("超时异常")
        def js_(self,text):
            self.driver.execute_script(text)
        def exit(self):
            self.driver.quit()