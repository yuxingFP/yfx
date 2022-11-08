import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from selenium import  webdriver
chrome = webdriver.Chrome()
# chrome = webdriver.Edge()
chrome.get("http://10.51.170.1:41570/eac/dap/mapp/std-eac-appcenter/index.html#/login")#进入基础管理平台
chrome.maximize_window()
sleep(2)
chrome.find_element(By.XPATH,"/html/body/div/section/div/div[6]/div/div[2]/form/div[1]/div/div/input").send_keys("zzpt02")
chrome.find_element(By.XPATH,"/html/body/div/section/div/div[6]/div/div[2]/form/div[2]/div/div/input").send_keys("1234.abcd1")

sleep(3)
chrome.find_element(By.XPATH,"/html/body/div/section/div/div[6]/div/div[2]/form/button").click()#login
chrome.implicitly_wait(10)
def parameter_management():#参数管理
    chrome.find_element(By.XPATH,'/html/body/div/section/main/div[1]/div[2]/div/div[2]/div/div[2]/div').click()
    # 点击分析参数管理菜单
    sleep(2)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[1]/div/div/input").send_keys("REALINSIGHT_WORKTABLE_PAGE_URL")
    # 输入查询的参数代码
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[2]/span").click()
    # 点击查询
    sleep(2)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[1]/div/div/div/div/div[2]/button[1]").click()
    # 点击编辑
    sleep(2)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div/div/div[3]/span/button[2]").click()
    # 点击确定（无更改操作）
    sleep(2)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[1]").click()
    # 点击重置
    sleep(3)
    print("参数管理测试成功结束")

def theme_management():#主题域管理
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[1]/div[2]/div/div[2]/div/div[3]").click()
    #点击主题域管理菜单
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/form/div/div/div/div/input").send_keys("hyx")
    sleep(1)
    # chrome.save_screenshot("yfx.png")
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[1]/div/div/div/div/div[2]/button[2]").click()
    sleep(1)
    # 名称查询过滤
    chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/div[2]/section/main/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[4]/td[4]/div[1]").click()
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[1]/div/div/div/div/div[2]/button[1]").click()
    print("主题域管理测试成功结束")

def service_management():#服务资源管理
    chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/div[1]/div[2]/div/div[2]/div/div[4]").click()
    #点击服务资源管理
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[1]/div/div/div/input").send_keys("币种")
    #在服务名称筛选框输入：币种
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[7]/div[1]/div[1]/ul/li/div/span").click()#/html/body/div[7]/div[1]/div[1]/ul/li/div/span
    #选中：标准-币种名称转换服务
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[2]").click()
    # 点击查询
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[4]/div/div").click()
    # 选中服务，显示查看界面
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div/div[1]/button/i").click()
    #退出查看界面
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[1]").click()
    #点击重置按钮
    sleep(1)

    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[2]/div/div/div/div/input").click()
    # 点击服务性质下拉框
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[9]/div[1]/div[1]/ul/li[1]/span").click()
    # 选中数据源服务
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[2]").click()
    #点击查询
    sleep(1)
    chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[1]").click()
    # 点击重置按钮
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[3]/div/div/div/div[1]/input").click()
    #点击接口类型下拉框
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[10]/div[1]/div[1]/ul/li[1]/span").click()
    #选中微服务
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[2]").click()
    # 点击查询
    sleep(1)
    chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[1]").click()
    # 点击重置按钮
    sleep(1)
    print("服务资源管理测试成功结束")

def data_management():#数据源管理
    chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/div[1]/div[2]/div/div[2]/div/div[5]").click()
    #点击数据源管理菜单
    sleep(3)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[1]/div/div/div[1]/input").send_keys("SJY1")
    #输入模型代码
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[2]").click()
    # 查询
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[4]/div/div/a").click()
    #点击第一条数据代码，进入查看
    sleep(2)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div/div[2]/div/div/div[2]/button").click()
    #进行测试连接
    # attribute = chrome.find_element(By.XPATH, "/html/body/div[10]").get_attribute("innerText")
    # print(attribute)
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div/div[1]/button/i").click()
    # 退出查看界面
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[1]").click()
    # 点击重置按钮
    sleep(1)

    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[2]/div/div/div/input").send_keys("易分析")
    # 数据源筛选
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[2]").click()
    # 查询
    sleep(1)
    data_name= chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[5]/div/div").get_attribute("innerText")
    print(data_name)
    #打印第一条数据源的名称
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[1]").click()
    # 点击重置按钮
    sleep(1)

    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[3]/div/div/div/input").click()
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[11]/div[1]/div[1]/ul/li[2]").click()
    # chrome.find_element(By.XPATH,"/html/body/div[10]/div[1]/div[1]/ul/li[1]").click()#单独运行一个模型快时使用
    #连接方式

    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[4]/div/div/button[2]").click()
    # 查询
    sleep(1)
    data_name_2 = chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[5]/div/div").get_attribute(
        "innerText")
    print(data_name_2)
    # 打印第一条数据源的名称
    sleep(1)
    print("数据源管理测试成功结束")

def date_conversion():#数据转换模型
    chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/div[1]/div[2]/div/div[2]/div/div[6]").click()
    # 点击数据源管理菜单
    sleep(3)
    # chrome.refresh()
    # str_2 = chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[4]/div/div/a")
    str_1 = chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/main/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[4]/div/div/a").text
    print(str_1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[1]/div/div/input").send_keys(str_1)
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[6]/div/div/button[2]").click()
    # 点击查询
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[3]/div/div/div/table/tbody/tr/td[2]/div[1]/div").click()
    # chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[3]/div/div/div/table/tbody/tr/td[2]/div[1]").send_keys(Keys.DOWN)
    sleep(2)
    chrome.find_element(By.XPATH,"//table[@class='component_ui_listview_list_table']").find_element(By.XPATH,"//tbody/tr[4]/td/table/tbody/tr/td[5]").click()
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[6]/div/div/button[2]").click()
    sleep(2)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/header/div[2]/div/div[2]/div/form/div[6]/div/div/button[1]").click()
    sleep(1)
    print("数据分析模型测试完成")

def custom_management():
    chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/div[1]/div[2]/div/div[2]/div/div[7]").click()
    #点击自定义分析模型管理菜单
    sleep(1)
    elements = chrome.find_elements(By.XPATH, "//div[@class='btn-slot']/button")
    print(len(elements))#5个基础按钮
    elements[1].click()#点击新增
    str_ = "HYX自动化测试" + str(int(time.time()))#设置模型名称
    print(str_)
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/form/div[1]/div[2]/div/div/div/input").send_keys(str_)
    #模型名称输入
    sleep(2)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/form/div[2]/div[1]/div/div/div/div/div[1]/input").click()
    # 点击数据源选项
    sleep(1)
    find_elements = chrome.find_elements(By.XPATH, "//span[text()='易分析本地数据源']")
    # 选中每一个数据源（li存在15个）
    print(len(find_elements))
    sleep(2)
    find_elements[1].click()
    # 选择第一个数据源
    sleep(2)
    chrome.find_element(By.XPATH,'/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/form/div[2]/div[2]/div/div/div/div/table/tbody/tr/td[2]/div[1]/div').click()
    # 点击主题域
    sleep(2)
    try:
        chrome.find_elements(By.XPATH,"//td[text()='报账中心']")[1].click()
    except:
        chrome.find_element(By.XPATH, "//td[text()='报账中心']").click()
    finally:

        # 选中一个主题域
        sleep(2)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/button").click()
        # 点击选择表
        sleep(2)
        chrome.find_element(By.XPATH,"/html/body/div[20]/div/div[2]/div/div/div/div[1]/div/div[1]/div/input").send_keys('a')
        # 在搜索栏中填入搜索关键字
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[20]/div/div[2]/div/div/div/div[1]/div/div[2]/button").click()
        # 点击查询
        sleep(10)
        chrome.find_element(By.XPATH,"/html/body/div[20]/div/div[2]/div/div/div/div[2]/div[1]/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[5]/td[4]/div").click()
        # 选中一个表
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[20]/div/div[3]/span/div/button[2]").click()
        # 点击确定
        sleep(2)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[5]/div[1]/div").click()
        # 选中表名称选项
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[5]/div[1]/div[2]/table/tbody/tr/td[2]/textarea").send_keys("hhh")
        # 填入表名称
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/table/tbody/tr/td[1]/div[1]/span/table[1]/tbody/tr[3]/td[6]/div[1]/div").click()
        # 点击表类型
        sleep(1)
        chrome.find_element(By.XPATH,"//td[text()='普通表']").click()
        # 选择普通表
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[4]/button").click()
        # 点击下一步
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/button[1]").click()
        # 点击选择字段
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[2]/table[1]/tbody/tr[2]/td[2]/div/table/tbody/tr/td[1]/div").click()
        # 勾选全部
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[2]/div/div[3]/span/div/button[2]").click()
        # 点击确定
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/button[2]").click()
        # 点击下一步
        sleep(2)
        attribute = chrome.find_element(By.XPATH, "/html/body/div[35]/div/div[1]/p").get_attribute("innerText")
        print(attribute)
        chrome.find_element(By.XPATH,"/html/body/div[35]/div/div[2]").click()
        sleep(1)
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[1]/button/i").click()
        # chrome.find_element(By.XPATH,"/html/body/div[20]/div/div[3]/span/div/button[1]").click()
        # #单独运行第三个层级的div选19，同时运行时div选20
        # sleep(2)
        # chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[3]/span/button[2]").click()
        # sleep(2)
def model_management():
    chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/div[1]/div[2]/div/div[2]/div/div[8]").click()
    # 点击分析模型管理菜单
    sleep(1)
    elements = chrome.find_elements(By.XPATH, "/html/body/div[1]/section/main/div[2]/section/main/div/div/div[1]/div/div/div/div/div[2]/button")
    print(len(elements))  # 5个基础按钮
    elements[1].click()  # 点击新增
    sleep(1)
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div[1]/input").click()
    sleep(1)
    find_elements = chrome.find_elements(By.XPATH, "//span[text() = '业务单据']")
    print(len(find_elements))
    find_elements[1].click()
    sleep(1)
    # 定位业务单据方法一
            # find_elements_1 = chrome.find_elements(By.XPATH, "//ul[@class = 'el-scrollbar__view el-select-dropdown__list']/li")
            # print(len(find_elements_1))
            # find_elements_1[4].click()
            # sleep(1)
            # 定位业务单据方案2
    chrome_find_elements = chrome.find_elements(By.XPATH,"//table[@ecpclass='ecp.ui.datafield.Grid']")
    print(len(chrome_find_elements))
    # chrome_find_elements[1].find_element(By.XPATH,"//tbody/")
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]/div[2]/table[1]/tbody/tr[3]/td[2]/div/table/tbody/tr/td[1]/div").click()
    sleep(2)
    # 勾选一个模型
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/button[2]").click()
    sleep(1)
    # 确定
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/form/div[1]/div[2]/div/div/div/div/table/tbody/tr/td[2]/div[1]/div").click()
    sleep(1)
    # 点击选择主题域选项
    l = chrome.find_elements(By.XPATH, "//td[text()='凭证分录查询']")
    print(len(l))
    l[1].click()
    # chrome.find_element(By.XPATH,"/html/body/div[18]/div/table/tbody/tr/td[1]/div/table/tbody/tr[6]/td/table/tbody/tr/td[5]")
    # chrome.find_element(By.XPATH,"/html/body/div[17]/div/table/tbody/tr/td[1]/div/table/tbody/tr[6]/td/table/tbody/tr/td[5]").click()
    sleep(1)
    # 选择主题域
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr/td[1]/div[2]/table[1]/tbody/tr[2]/td[2]/div/table/tbody/tr/td[1]/div").click()
    sleep(1)
    # 勾选全部字段
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/input").clear()
    sleep(1)
    # 清空表名
    chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/input").send_keys("hyx"+str(int(time.time())))
    # 修改表名
    sleep(1)
    try:
        chrome.find_element(By.XPATH,"/html/body/div[1]/section/main/div[2]/section/div/div/div[1]/div/div[2]/div[2]/button[3]").click()
        sleep(2)
    except:
        print("保存异常")


# #
parameter_management()
theme_management()
service_management()
data_management()
date_conversion()
custom_management()
model_management()
# chrome.quit()


