from po.page import Page
from selenium.webdriver.common.by import By
class Custom_model(Page):
    # 自定义分析模型管理
    menu = (By.XPATH, "//span[text()='自定义分析模型管理']")
    new_add = (By.XPATH,"//span[text()='新增']")
    name = (By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/form/div[1]/div[2]/div/div/div/input")
    data_scourse = (By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/form/div[2]/div[1]/div/div/div/div/div[1]/input")
    option = (By.XPATH,"//span[text()='易分析测试数据库（85.23库）-勿删']")
    theme_opt = (By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/form/div[2]/div[2]/div/div/div/div/table/tbody/tr/td[2]/div[1]/div")
    option_2 = (By.XPATH, "//span[text()='报账中心']")
    button_opt = (By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/button")

