import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from lxml import etree
import codecs


def config_browser():
    browser = webdriver.Chrome()
    return browser


def get_first_page(browser, url):
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
    browser.execute_script("arguments[0].value = '{:s}'".format(start), date_start)
    date_end = browser.find_element_by_xpath('//*[@id="txtEndDate"]')
    browser.execute_script("arguments[0].value = '{:s}'".format(end), date_end)

    browser.find_element_by_xpath('//*[@id="imgSearch"]').click()
    time.sleep(1)
    browser.switch_to_window(browser.window_handles[1])
    return browser


start = "2020-06-01"
end = "2020-06-30"
url = "https://satellite.nsmc.org.cn/portalsite/Data/Satellite.aspx"
url2 = "https://satellite.nsmc.org.cn/portalsite/Data/FileShow.aspx"
browser = config_browser()
browser = get_first_page(browser, url)

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
            try:
                print(fname[0].attrib.get("title"))
            except:
                print("done!")
                break
        try:
            browser.find_element_by_link_text("下一页").click()
        except:
            print("done!")
            break
    time.sleep(1)
    html = browser.execute_script("return document.documentElement.outerHTML")
    time.sleep(2)
    tree = etree.HTML(html)
    flag = tree.xpath('//*[@id="inf_0"]')
browser.quit()
