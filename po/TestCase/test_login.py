import os

import pytest
import pytest_html
from po.pages.loginpage import LoginPage
from po.pages.parameter_management import Parameter_management_page
from po.pages.theme_management import Theme_management
from selenium import webdriver




class Test_yfx():
    driver = webdriver.Chrome()
    url = "http://10.51.170.1:41570/eac/dap/mapp/std-eac-appcenter/index.html#/login"
    username = "zzpt02"
    password = "1234.abcd1"
    text = "hyx"
    def test_login(self):
        page = LoginPage(self.driver)
        page.open(self.url)
        page.user_input(self.username)
        page.pwd_input(self.password)
        page.sub_login()

    def test_menu_1(self):
        page = Parameter_management_page(self.driver)
        page.click_menu_1()
        page.send_keys_filter_1()
        page.click_search_1()
        page.click_see_1()
        page.click_close_1()
        page.click_reset_1()
    def test_menu_2(self):
        page = Theme_management(self.driver)
        page.click_menu()
        page.send_keys_filter_1(self.text)
        # page.click_data()
        page.click_button_3()
        # page.input()
        # page.send_keys_input_1(text2)

# if __name__ == '__main__':
#     # test_login(driver, url, username)
#     # # menu_1(driver)
#     # menu_2(driver,"hyx")
#     pytest.main()
#     os.system('allure generate ./temp -o ./report --clean')

