from po.page import Page
from selenium.webdriver.common.by import By
class Theme_management(Page):
    menu = (By.XPATH,"//span[text()='分析主题域管理']")
    #分析主题域管理
    filter_1 = (By.XPATH, "/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/form/div/div/div/div/input")
    #筛选框
    data = (By.XPATH, "/html/body/div[7]/div[1]/div[1]/ul/li/div")
    #下拉框
    button_3 = (By.XPATH, "//span[text()='新增下级']")
    #新增下级按钮
    input_1=(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[4]/td[4]/div[1]/table/tbody/tr/td[4]/div/div")
    # 新增下级div
    js = "document.querySelector('#qzzgrid1667199340031 > tbody > tr:nth-child(4) > td.gridEditFocusCell.gridCellRelative > div.winStyle').innerText='hanyuxing'"
    def click_menu(self):
        #点解分析主题域管理模块
        self.find_element(*self.menu).click()
    def send_keys_filter_1(self,text):
        self.find_element(*self.filter_1).send_keys(text)
        # 输入查询关键字
    def click_data(self):
        # 点击数据
        self.find_element(*self.data).click()
    def click_button_3(self):
        #点击新增下级
        self.find_element(*self.button_3).click()
    # def send_keys_input_1(self,text):
    #     self.find_element(*self.input_1).send_keys(text)
    def input(self):
        # 输入新增数据
        self.js_(self.js)



