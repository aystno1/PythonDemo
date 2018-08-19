#coding=utf-8

# 具体的selenium的方法需要你详细去翻翻它的[文档]
# http://selenium-python.readthedocs.io/

from selenium import webdriver
import logging
import logging.config
import os
# import pandas as pd
import csv
import requests
import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class DriverBuilder():
    def enable_download_in_headless_chrome(self, driver, download_dir):
        """ there is currently a "feature" in chrome where headless does not allow file download: https://bugs.chromium.org/p/chromium/issues/detail?id=696481
        This method is a hacky work-around until the official chromedriver support for this. Requires chrome version 62.0.3196.0 or above. """
        #add missing support for chrome "send_command" to selenium webdriver
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        command_result = driver.execute("send_command", params)

        for key in command_result:
            logging.getLogger().info("result:  （%s, %s）", key, str(command_result[key]))


def job_geturl1():
    try:
        # 设置chrome参数
        dir = Get_Download_Dir()
        # 构造模拟浏览器
        # firefox_login=webdriver.Firefox()
        # chrome_driver = webdriver.Chrome()
        # chrome_driver = webdriver.PhantomJS()
        logging.getLogger().info("文件下载路径是：%s",dir)
        chrome_options = webdriver.ChromeOptions()
        #logging.getLogger().info("1")
        prefs = {
            'profile.default_content_settings.popups': 0,
            'download.default_directory': dir,               # 设置下载文件路径
            # "profile.managed_default_content_settings.images": 2
        }
        #logging.getLogger().info("2")
        chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('--headless')
        # 以管理员身份打开
        chrome_options.add_argument('--no-sandbox')
        #logging.getLogger().info("3")
        chrome_driver = webdriver.Chrome(options=chrome_options)
        logging.getLogger().info("打开网址。。。")
        # 打开网址
        chrome_driver.get('http://www.stat-search.boj.or.jp/ssi/cgi-bin/famecgi2?cgi=$nme_a000_en&lstSelection=LA01')
        # 窗口最大化，可有可无，看情况
        # chrome_driver.maximize_window()

        chrome_driver.find_element_by_xpath('.//table[@class=\'menuSelect\']/tbody/tr[2]').click()
        chrome_driver.find_element_by_xpath('.//div[@class=\'nodeMenu\']/div[2]/input').click()
        chrome_driver.find_element_by_xpath('.//table[@class=\'menuSelect\']/tbody/tr[1]').click()
        chrome_driver.find_element_by_xpath('.//div[@class=\'nodeMenu\']/div[2]/input').click()
        chrome_driver.find_element_by_xpath('.//table[@class=\'menuSelect\']/tbody/tr[1]').click()
        chrome_driver.find_element_by_xpath('.//div[@class=\'nodeMenu\']/div[2]/input').click()
        chrome_driver.find_element_by_xpath('html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[1]/label').click()
        chrome_driver.find_element_by_xpath('html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[4]/a').click()
        chrome_driver.find_element_by_xpath('.//*[@id=\'fromYear\']').clear()
        chrome_driver.find_element_by_xpath('.//*[@id=\'fromYear\']').send_keys('1992')
        chrome_driver.find_element_by_xpath('.//*[@id=\'convert\']/select[1]/option[6]').click()
        chrome_driver.find_element_by_xpath('.//*[@id=\'resultArea\']/div[4]/div[1]/a[1]').click()
        # 获取所有打开窗口的句柄
        handles = chrome_driver.window_handles
        print(handles)
        # 切换窗口句柄
        chrome_driver.switch_to.window(handles[1])
        print(chrome_driver.current_window_handle)
        print(chrome_driver.title)

        chrome_driver.find_element_by_xpath('html/body/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/a').click()
        # 获取所有打开窗口的句柄
        handles1 = chrome_driver.window_handles
        print(handles1)
        # 切换窗口句柄
        chrome_driver.switch_to.window(handles1[2])
        url = chrome_driver.find_element_by_xpath('html/body/div[2]/div/div/center/div/table/tbody/tr/td/a').text
        csvurl = "http://www.stat-search.boj.or.jp/ssi/html" + url
        print(csvurl)
        chrome_driver.close()
        chrome_driver.switch_to.window(handles1[1])
        chrome_driver.close()
        chrome_driver.switch_to.window(handles1[0])
        chrome_driver.refresh()
        handles1 = []
        print("#12")
        #1 ==================
        chrome_driver.find_element_by_xpath('.//table[@class=\'menuSelect\']/tbody/tr[1]').click()
        chrome_driver.find_element_by_xpath('.//div[@class=\'nodeMenu\']/div[2]/input').click()
        chrome_driver.find_element_by_xpath('.//table[@class=\'menuSelect\']/tbody/tr[2]').click()
        chrome_driver.find_element_by_xpath('.//div[@class=\'nodeMenu\']/div[2]/input').click()
        chrome_driver.find_element_by_xpath('html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[1]/label').click()
        chrome_driver.find_element_by_xpath('html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[4]/a').click()
        chrome_driver.find_element_by_xpath('.//*[@id=\'fromYear\']').clear()
        chrome_driver.find_element_by_xpath('.//*[@id=\'fromYear\']').send_keys('1992')
        chrome_driver.find_element_by_xpath('.//*[@id=\'convert\']/select[1]/option[6]').click()
        chrome_driver.find_element_by_xpath('.//*[@id=\'resultArea\']/div[4]/div[1]/a[1]').click()
        print("#15")
        #1 ==================
        chrome_driver.find_element_by_xpath('.//table[@class=\'menuSelect\']/tbody/tr[1]').click()
        chrome_driver.find_element_by_xpath('.//div[@class=\'nodeMenu\']/div[2]/input').click()
        chrome_driver.find_element_by_xpath('.//table[@class=\'menuSelect\']/tbody/tr[5]').click()
        chrome_driver.find_element_by_xpath('.//div[@class=\'nodeMenu\']/div[2]/input').click()
        chrome_driver.find_element_by_xpath('html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[1]/label').click()
        chrome_driver.find_element_by_xpath('html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[4]/a').click()
        chrome_driver.find_element_by_xpath('.//*[@id=\'fromYear\']').clear()
        chrome_driver.find_element_by_xpath('.//*[@id=\'fromYear\']').send_keys('1992')
        chrome_driver.find_element_by_xpath('.//*[@id=\'convert\']/select[1]/option[6]').click()
        chrome_driver.find_element_by_xpath('.//*[@id=\'resultArea\']/div[4]/div[1]/a[1]').click()

        # 1 ==================
        chrome_driver.find_element_by_xpath('.//table[@class=\'menuSelect\']/tbody/tr[1]').click()
        chrome_driver.find_element_by_xpath('.//div[@class=\'nodeMenu\']/div[2]/input').click()
        chrome_driver.find_element_by_xpath('.//table[@class=\'menuSelect\']/tbody/tr[6]').click()
        chrome_driver.find_element_by_xpath('.//div[@class=\'nodeMenu\']/div[2]/input').click()
        chrome_driver.find_element_by_xpath('html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[1]/label').click()
        chrome_driver.find_element_by_xpath('html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[4]/a').click()
        chrome_driver.find_element_by_xpath('.//*[@id=\'fromYear\']').clear()
        chrome_driver.find_element_by_xpath('.//*[@id=\'fromYear\']').send_keys('1992')
        chrome_driver.find_element_by_xpath('.//*[@id=\'convert\']/select[1]/option[6]').click()
        chrome_driver.find_element_by_xpath('.//*[@id=\'resultArea\']/div[4]/div[1]/a[1]').click()
        # parse_csv(csvurl)
        # chrome_driver.find_element_by_xpath('html/body/div[2]/div/div/center/div/table/tbody/tr/td/a').click()
        # 浏览器退出
        chrome_driver.quit()
    except Exception as err:
        logging.getLogger().error(err)


def parse_csv(urls):
    print("下载地址是：%s" % (urls))
    # 转换成Excel
    r = requests.get(urls)
    with open("download/test1.csv", "wb") as code:
        code.write(r.content)
    print("csv存入download...")
    # # 新建excel文件
    myexcel = xlwt.Workbook()
    # # 新建sheet页
    mysheet = myexcel.add_sheet("sheet1")
    # 读取csv
    csvfile = open("download/test1.csv","rb")
    print("读取csv...")
    
    # 读取文件信息
    reader = csv.reader(csvfile)
    l = 0
    # 通过循环获取单行信息
    for line in reader:
        r = 0
        # 通过双重循环获取单个单元信息
        for i in line:
            # print l,r
            # 通过双重循环写入excel表格
            mysheet.write(l,r,i)
            r=r+1
        l=l+1
    # 最后保存到excel
    print("写入...")
    # savepath = unicode("../macroSpider/japantest/myexcel.xls","utf8")
    myexcel.save("../macroSpider/Japan Domestically Licensed Banks/myexcel.xls")
    print("保存csv...")
    # csv = pd.read_csv(urls, encoding='utf-8')
    # csv.to_excel('download/2.xlsx', sheet_name='data')


def Get_Download_Dir():
    download_dir = os.getcwd() + "/download"
    if os.path.exists(download_dir) == False:
        logging.getLogger().info("未检索到下载目录,新建目录: %s", download_dir)
        os.mkdir(os.getcwd() + "/download")
    else:
         logging.getLogger().info("下载目录: %s", download_dir)

    bak_download_dir = os.getcwd() + "/bak_download"
    if os.path.exists(bak_download_dir) == False:
        logging.getLogger().info("未检索到备份目录,新建备份目录: %s", bak_download_dir)
        os.mkdir(os.getcwd() + "/bak_download")
    else:
        logging.getLogger().info("备份目录: %s", bak_download_dir)

    return download_dir


def init():
    #创建logs文件夹
    log_dir = os.getcwd() + "/logs"
    if os.path.exists(log_dir) == False:
        os.mkdir(os.getcwd() + "/logs")
    logging.config.fileConfig("conf/conf_log.txt", defaults={'logdir': "logs"})


if __name__ == '__main__':
    # init()
    job_geturl1()
    # parse_csv("http://www.stat-search.boj.or.jp/ssi/html/nme_R031.754.20180816101410.01.csv")
