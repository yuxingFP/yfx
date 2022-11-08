from po.page import Page
from selenium.webdriver.common.by import By
class Parameter_management_page(Page):
    menu_1=(By.XPATH, '/html/body/div/section/main/div[1]/div[2]/div/div[2]/div/div[2]/div')
    # 参数管理模块
    filter_1=(By.XPATH, "/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[1]/div/div/input")
    # 参数代码过滤
    frist_data=(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[4]/div/div")
    # 第一行参数代码定位
    search_1 = (By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[2]")
    # 查询按钮
    see_1 = (By.XPATH, "/html/body/div[1]/section/main/div[2]/section/main/div/div/div[1]/div/div/div/div/div[2]/button[2]")
    # 查看按钮
    close_1 = (By.XPATH, "/html/body/div[1]/section/main/div[2]/section/div/div/div/div/div[3]/span/button[1]")
    # 关闭查看
    reset_1 =(By.XPATH, "/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[1]")
    # 重置按钮
    def click_menu_1(self):# 点击菜单
        self.find_element(*self.menu_1).click()
    def send_keys_filter_1(self):# 输入筛选条件
        attribute = self.find_element(*self.frist_data).get_attribute("innerText")
        self.find_element(*self.filter_1).send_keys(attribute)
    def click_search_1(self):# 查询
        self.find_element(*self.search_1).click()
    def click_see_1(self):# 查看
        self.find_element(*self.see_1).click()
    def click_close_1(self):# 关闭查看
        self.find_element(*self.close_1).click()
    def click_reset_1(self):# 重置过滤条件
        self.find_element(*self.reset_1).click()


