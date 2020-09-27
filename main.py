import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from lxml import etree
import codecs

url = "https://satellite.nsmc.org.cn/portalsite/Data/Satellite.aspx"
url2 = "https://satellite.nsmc.org.cn/portalsite/Data/FileShow.aspx"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(10)
browser.find_element_by_xpath(
    '//*[@id="FY4A-_AGRI--_N_DISK_1047E_L1-_GEO-_MULT_NOM_YYYYMMDDhhmmss_YYYYMMDDhhmmss_4000M_V0001.HDF"]').click()
browser.find_element_by_xpath(
    '//*[@id="FY4A-_AGRI--_N_DISK_1047E_L1-_FDI-_MULT_NOM_YYYYMMDDhhmmss_YYYYMMDDhhmmss_4000M_V0001.HDF"]').click()
browser.find_element_by_xpath(
    '//*[@id="FY4A-_AGRI--_N_REGC_1047E_L1-_GEO-_MULT_NOM_YYYYMMDDhhmmss_YYYYMMDDhhmmss_4000M_V0001.HDF"]').click()
browser.find_element_by_xpath(
    '//*[@id="FY4A-_AGRI--_N_REGC_1047E_L1-_FDI-_MULT_NOM_YYYYMMDDhhmmss_YYYYMMDDhhmmss_4000M_V0001.HDF"]').click()
date_start = browser.find_element_by_xpath('//*[@id="txtBeginDate"]')
browser.execute_script("arguments[0].value = '2020-06-01'", date_start)
date_end = browser.find_element_by_xpath('//*[@id="txtEndDate"]')
browser.execute_script("arguments[0].value = '2020-06-30'", date_end)

browser.find_element_by_xpath('//*[@id="imgSearch"]').click()
time.sleep(1)
browser.switch_to_window(browser.window_handles[1])
while True:
    html = browser.execute_script("return document.documentElement.outerHTML")
    time.sleep(2)
    tree = etree.HTML(html)
    flag = tree.xpath('//*[@id="inf_0"]')

    if len(flag) > 0:
        break
    else:
        flag_pre_str = ""

while True:
    flag_str = flag[0].attrib.get("title")
    if flag_str != flag_pre_str:
        flag_pre_str = flag_str
        for i in range(30):
            fname = tree.xpath('//*[@id="inf_{:d}"]'.format(i))
            print(fname[0].attrib.get("title"))
        browser.find_element_by_xpath('//*[@id="pager"]/div/a[7]').click()
        time.sleep(1)
    html = browser.execute_script("return document.documentElement.outerHTML")
    time.sleep(2)
    tree = etree.HTML(html)
    flag = tree.xpath('//*[@id="inf_0"]')