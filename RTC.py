# 缺陷单
# 导入模块：
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time
from os import path
from time import sleep
# from docx import doctest
from selenium import webdriver
# from win32com import client as wc
# import docx
# import os
# import re
# import codecs
# import sys
# 不自动关闭浏览器
# from test import handles
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
# 读取参数
with open("BUG.txt","r",encoding='utf-8') as file:
    l = file.readlines()  # 按行读取TXT文件，都是字符串类型
    d = {}
    for i in l:
        s = i.replace('\n', '')  # 去除换行符
        s0 = s.split(sep=':')  # 以:分割字符串，左边是键，右边是值。同样都是字符串类型
        if '"' in s0[1]:
            s0[1] = s0[1].replace('"', '')  # 字符串存在双引号，说明原本的值就是字符串类型。去掉多余的双引号
        else:
            s0[1] = int(s0[1])  # 说明原本值是整型，强制类型转换
        d[s0[0]] = s0[1]  # 键值对添加到字典中
    print(f"\033[36m{d}\033[0m")

# 变量赋值
zhaiyao = d['zhaiyao']
banbenghao = d['banbenghao']
xitong = d['xitong']
mokuai = d['mokuai']
diedai_jieduan = d['diedai_jieduan']
gushi_danhao = d['gushi_danhao']
kaifa_name = d['kaifa_name']
zhanghao = d['zhanghao']
mima = d['mima']

# 此处添加了chrome_options参数
# driver = webdriver.Firefox()    #火狐
driver = webdriver.Chrome()        #谷歌
driver.get('https://rdm.ygsoft.com:9443/ccm/web/projects/GRIS%E9%A1%B9%E7%9B%AE#action=com.ibm.team.workitem.newWorkItem&type=com.ygsoft.billType.testProblem&ts=16625296324670')
# 改变浏览器大小:
# driver.set_window_size(520,520)
# 全屏显示
driver.maximize_window()
# 安全提示：
driver.find_element(By.ID,"details-button").click()
driver.find_element(By.ID,"proceed-link").click()
# 登录账号

driver.find_element(By.ID,"jazz_app_internal_LoginWidget_0_userId").send_keys(zhanghao)
driver.find_element(By.ID,"jazz_app_internal_LoginWidget_0_password").send_keys(mima)
# 定位登录按钮
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div[3]/form/button").click()
sleep(8)
# 设定隐式等待:
driver.implicitly_wait(5)
# 获取当前窗口的句柄
a = driver.current_window_handle
#*******************************输入缺陷单详情***************************************
driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[3]/div/div/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]").send_keys(zhaiyao)
# 填版本号
driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[3]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/div/table/tbody/tr[3]/td/div/div[2]/span[3]").click()
driver.find_element(By.XPATH,"/html/body/div[9]/div[1]/input").send_keys(banbenghao)
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[9]/div[2]/div[1]/ul/li[3]").click()
time.sleep(1)
# driver.find_element(Keys.ARROW_DOWN)
# 系统
driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[3]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/div/table/tbody/tr[5]/td/div/div[2]/span[3]").click()
time.sleep(1)
# *******************************输入对应的系统**************************************
driver.find_element(By.XPATH,"/html/body/div[9]/div[1]/input").send_keys(xitong)
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[9]/div[2]/div[1]/ul/li[1]").click()
time.sleep(1)
# 模块
driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[3]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/div/table/tbody/tr[6]/td/div/div[2]").click()
time.sleep(1)
# *******************************输入对应的模块**************************************
driver.find_element(By.XPATH,"/html/body/div[9]/div[1]/input").send_keys(mokuai)
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[9]/div[2]/div[1]/ul/li[1]").click()
time.sleep(1)
# 迭代阶段
driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[3]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/div/table/tbody/tr[11]/td/div/div[2]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[9]/div[1]/span/a/img").click()
time.sleep(2)
#*******************************对应的迭代阶段***************************************
driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div[2]/div[3]/div/div/div[1]/input").send_keys(diedai_jieduan)
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[2]").click()
driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div[2]/div[3]/div/div/div[3]/button[1]").click()
time.sleep(1)
# 添加故事单号
driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[3]/div/div/div/div[3]/div/div/div/div[1]/div[3]/div/div/div[3]/div/div/div[1]/div/div[2]/span[1]").click()
time.sleep(1)
#*******************************输入故事单号***************************************
driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div[2]/div[3]/div/div/div[3]/div[2]/div/input").send_keys(gushi_danhao)
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div[2]/div[3]/div/div/div[7]/select/option").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div[2]/div[3]/div/div/div[9]/button[1]").click()
time.sleep(1)
# 接收人
driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[3]/div/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/div/div[2]").click()
time.sleep(1)
# *******************************输入对应的开发姓名***************************************
driver.find_element(By.XPATH,"/html/body/div[9]/div[1]/input").send_keys(kaifa_name)
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[9]/div[2]/div[3]/ul/li").click()
time.sleep(1)

# 保存
driver.find_element(By.XPATH,"/html/body/div[1]/div/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/div[3]/div/div/div/div[1]/div[1]/span/span[3]/span/button[2]").click()
time.sleep(1)
# 提交开发
driver.find_element(By.XPATH,'//*[@id="com_ibm_team_workitem_web_ui_internal_view_editor_parts_StatusAttributePart_2"]/div/select').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="com_ibm_team_workitem_web_ui_internal_view_editor_parts_StatusAttributePart_2"]/div/select/option[2]').click()
time.sleep(1)
# 保存提交
driver.find_element(By.XPATH,'//*[@id="com_ibm_team_workitem_web_ui_internal_view_editor_WorkItemEditorHeader_1"]/div[1]/span/span[3]/span/button[2]').click()
# 截图验证
# driver.get_screenshot_as_file('C:\Users\少禹\Desktop\cs.png')
# 关闭浏览器
# driver.quit()



