from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

#爬取各年份的招生、在校、毕业生数量
def data2017():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get('http://data.stats.gov.cn/tablequery.htm?code=AD0E')
    wait = WebDriverWait(driver, 10)
    try:
        #确保滚动条内容加载
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#tree')))
        #操作滚动条
        driver.execute_script('var q=document.documentElement.scrollTop=100000')
        #当元素可点击时点击
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#tree_26_a'))).click()
        #休眠3秒保证页面已经切换完毕
        time.sleep(3)
        #解析
        html=etree.HTML(driver.page_source)
        #定义数组存储数据
        results=[]
        #字段定义
        quota=html.xpath('//*[@id="tabledata"]//td[1]/text()')
        enrollment=html.xpath('//*[@id="tabledata"]//td[2]/text()')
        students=html.xpath('//*[@id="tabledata"]//td[3]/text()')
        graduate=html.xpath('//*[@id="tabledata"]//td[4]/text()')
        for quota,enrollment,students,graduate in zip(quota,enrollment,students,graduate):
            data={
                'quota':quota.lstrip().replace('#',''),
                'enrollment':int(enrollment),
                'students':int(students),
                'graduate':int(graduate)
            }
            results.append(data)
        return results
    except TimeoutException:
        print('Time Out')
    finally:
        driver.close()
def data2016():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get('http://data.stats.gov.cn/tablequery.htm?code=AD0E')
    wait = WebDriverWait(driver, 10)
    try:
        #确保内容加载
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#tree')))
        #操作滚动条
        driver.execute_script('var q=document.documentElement.scrollTop=100000')
        #当元素可点击时点击
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#tree_26_a'))).click()
        #确保下拉框加载完毕
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mySelect_sj')))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mySelect_sj .dtHead'))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mySelect_sj div.dtList > ul > li:nth-child(2)'))).click()
        time.sleep(3)
        html=etree.HTML(driver.page_source)
        results=[]
        #字段定义
        quota=html.xpath('//*[@id="tabledata"]//td[1]/text()')
        enrollment=html.xpath('//*[@id="tabledata"]//td[2]/text()')
        students=html.xpath('//*[@id="tabledata"]//td[3]/text()')
        graduate=html.xpath('//*[@id="tabledata"]//td[4]/text()')
        for quota,enrollment,students,graduate in zip(quota,enrollment,students,graduate):
            data={
                'quota':quota.lstrip().replace('#',''),
                'enrollment':int(enrollment),
                'students':int(students),
                'graduate':int(graduate)
            }
            results.append(data)
        return results
    except TimeoutException:
        print('Time Out')
    finally:
        driver.close()
def data2015():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get('http://data.stats.gov.cn/tablequery.htm?code=AD0E')
    wait = WebDriverWait(driver, 10)
    try:
        #确保内容加载
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#tree')))
        #操作滚动条
        driver.execute_script('var q=document.documentElement.scrollTop=100000')
        #当元素可点击时点击
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#tree_26_a'))).click()
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#mySelect_sj')))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mySelect_sj .dtHead'))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mySelect_sj div.dtList > ul > li:nth-child(3)'))).click()
        time.sleep(3)
        html=etree.HTML(driver.page_source)
        results=[]
        #字段定义
        quota=html.xpath('//*[@id="tabledata"]//td[1]/text()')
        enrollment=html.xpath('//*[@id="tabledata"]//td[2]/text()')
        students=html.xpath('//*[@id="tabledata"]//td[3]/text()')
        graduate=html.xpath('//*[@id="tabledata"]//td[4]/text()')
        for quota,enrollment,students,graduate in zip(quota,enrollment,students,graduate):
            data={
                'quota':quota.lstrip().replace('#',''),
                'enrollment':int(enrollment),
                'students':int(students),
                'graduate':int(graduate)
            }
            results.append(data)
        return results
    except TimeoutException:
        print('Time Out')
    finally:
        driver.close()
def data2014():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get('http://data.stats.gov.cn/tablequery.htm?code=AD0E')
    wait = WebDriverWait(driver, 10)
    try:
        #确保内容加载
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#tree')))
        #操作滚动条
        driver.execute_script('var q=document.documentElement.scrollTop=100000')
        #当元素可点击时点击
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#tree_26_a'))).click()
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#mySelect_sj')))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mySelect_sj .dtHead'))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mySelect_sj div.dtList > ul > li:nth-child(4)'))).click()
        time.sleep(3)
        html=etree.HTML(driver.page_source)
        results=[]
        #字段定义
        quota=html.xpath('//*[@id="tabledata"]//td[1]/text()')
        enrollment=html.xpath('//*[@id="tabledata"]//td[2]/text()')
        students=html.xpath('//*[@id="tabledata"]//td[3]/text()')
        graduate=html.xpath('//*[@id="tabledata"]//td[4]/text()')
        for quota,enrollment,students,graduate in zip(quota,enrollment,students,graduate):
            data={
                'quota':quota.lstrip().replace('#',''),
                'enrollment':int(enrollment),
                'students':int(students),
                'graduate':int(graduate)
            }
            results.append(data)
        return results
    except TimeoutException:
        print('Time Out')
    finally:
        driver.close()
def data2013():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get('http://data.stats.gov.cn/tablequery.htm?code=AD0E')
    wait = WebDriverWait(driver, 10)
    try:
        #确保内容加载
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#tree')))
        #操作滚动条
        driver.execute_script('var q=document.documentElement.scrollTop=100000')
        #当元素可点击时点击
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#tree_26_a'))).click()
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mySelect_sj')))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mySelect_sj .dtHead'))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mySelect_sj div.dtList > ul > li:nth-child(5)'))).click()
        time.sleep(3)
        html=etree.HTML(driver.page_source)
        results=[]
        #字段定义
        quota=html.xpath('//*[@id="tabledata"]//td[1]/text()')
        enrollment=html.xpath('//*[@id="tabledata"]//td[2]/text()')
        students=html.xpath('//*[@id="tabledata"]//td[3]/text()')
        graduate=html.xpath('//*[@id="tabledata"]//td[4]/text()')
        for quota,enrollment,students,graduate in zip(quota,enrollment,students,graduate):
            data={
                'quota':quota.lstrip().replace('#',''),
                'enrollment':int(enrollment),
                'students':int(students),
                'graduate':int(graduate)
            }
            results.append(data)
        return results
    except TimeoutException:
        print('Time Out')
    finally:
        driver.close()

#爬取各年份的总人口
def population():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    driver.get('http://data.stats.gov.cn/easyquery.htm?cn=C01')
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#treeZhiBiao')))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#treeZhiBiao_4_a'))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#treeZhiBiao_30_a'))).click()
        # 确保滚动条内容加载
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#table_main')))
        # 解析
        html = etree.HTML(driver.page_source)
        # 定义数组存储数据
        results = []
        # 字段定义
        year2017 = html.xpath('//*[@id="table_main"]//tr[1]/td[2]/text()')
        year2016 = html.xpath('//*[@id="table_main"]//tr[1]/td[3]/text()')
        year2015 = html.xpath('//*[@id="table_main"]//tr[1]/td[4]/text()')
        year2014 = html.xpath('//*[@id="table_main"]//tr[1]/td[5]/text()')
        year2013 = html.xpath('//*[@id="table_main"]//tr[1]/td[6]/text()')
        for year2017,year2016,year2015,year2014,year2013 in zip(year2017,year2016,year2015,year2014,year2013):
            data = {
                'year2017':int(year2017),
                'year2016':int(year2016),
                'year2015':int(year2015),
                'year2014':int(year2014),
                'year2013':int(year2013)
            }
            results.append(data)
        return results
    except TimeoutException:
        print('Time Out')
    finally:
        driver.close()