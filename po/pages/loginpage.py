from po.page import Page
from selenium.webdriver.common.by import By
class LoginPage(Page):
    user_loc=(By.XPATH,"/html/body/div/section/div/div[6]/div/div[2]/form/div[1]/div/div/input")
    pass_loc=(By.XPATH,"/html/body/div/section/div/div[6]/div/div[2]/form/div[2]/div/div/input")
    submit = (By.XPATH,"/html/body/div/section/div/div[6]/div/div[2]/form/button")

    def user_input(self,username):
        self.find_element(*self.user_loc).send_keys(username)
    def pwd_input(self,password):
        self.find_element(*self.pass_loc).send_keys(password)
    def sub_login(self):
        self.find_element(*self.submit).click()