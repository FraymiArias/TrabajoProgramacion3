from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark
import os
import errno

def foto(driver,path):
    time.sleep(4)
    try:
        os.mkdir('SS/'+path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('SS/' + path + '/' + hora + '.png')

@mark.parametrize("email,password", [("admin@example.com", "123456"),
                                    ("employee@example.com", "123456"),
                                    ("client@example.com", "123456"),
                                    ("fake@example.com", "123456")])
def test_loginAdmin(email, password):
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    user = driver.find_element(By.XPATH, '//div[@class="body-wrapper clearfix"]//div[@class="col-md-12"]//p[2]').text
    foto(driver, 'LoginAdmin')
    assert driver.current_url == 'https://demo.worksuite.biz/account/dashboard' and user == 'Employee Id : EMP-1'

@mark.parametrize("email,password", [("admin@example.com", "123456"),
                                    ("employee@example.com", "123456"),
                                    ("client@example.com", "123456"),
                                    ("fake@example.com", "123456")])
def test_loginEmployee(email, password):
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit-login').click()
    user = driver.find_element(By.XPATH, '//div[@class="body-wrapper clearfix"]//div[@class="col-md-12"]//p[2]').text
    foto(driver, 'LoginEmployee')
    assert driver.current_url == 'https://demo.worksuite.biz/account/dashboard' and user == 'Employee Id : EMP-2'


@mark.parametrize("email,password", [("admin@example.com", "123456"),
                                    ("employee@example.com", "123456"),
                                    ("client@example.com", "123456"),
                                    ("fake@example.com", "123456")])
def test_loginClient(email, password):
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit-login').click()
    data = driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[2]/a').text
    foto(driver, 'LoginClient')
    assert driver.current_url == 'https://demo.worksuite.biz/account/dashboard' and data == 'Work'

def test_logout():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/ul/li[4]/div').click()
    foto(driver, 'logout')
    assert driver.current_url == 'https://demo.worksuite.biz/login'

def test_leadsdBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//div[@id="sideMenuScroll"]/ul/li[2]/a').click()
    foto(driver, 'leadsdBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/leads'

def test_clientsdBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[3]/a').click()
    foto(driver, 'clientsdBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/clients'

def test_hrBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[4]').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[4]/div/a[1]').click()
    foto(driver, 'hrBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/employees'    

def test_workContractsBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[1]').click()
    foto(driver, 'workContractsBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/contracts'

def test_workProjectsBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[2]').click()
    foto(driver, 'workProjectsBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/projects'

def test_tasksBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[3]').click()
    foto(driver, 'tasksBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/tasks'

def test_timeLogsBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[5]/div/a[4]').click()
    foto(driver, 'timeLogsBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/timelogs'

def test_productsBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[7]/a').click()
    foto(driver, 'productsBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/products'

def test_ordersBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[8]/a').click()
    foto(driver, 'ordersBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/orders'

def test_ticketsBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[9]/a').click()
    foto(driver, 'ticketsBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/tickets'

def test_eventsBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[10]/a').click()
    foto(driver, 'eventsBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/events'

def test_financeEstimatesBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[6]').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[6]/div/a[2]').click()
    foto(driver, 'financeEstimatesBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/estimates'

def test_financeInvoicesBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[6]').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[6]/div/a[3]').click()
    foto(driver, 'financeInvoicesBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/invoices'

def test_financePaymentsBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[6]').click()
    driver.find_element(By.XPATH, '//*[@id="sideMenuScroll"]/ul/li[6]/div/a[4]').click()
    foto(driver, 'financePaymentsBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/payments'

def test_logoutMenuBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="dropdownMenuLink"]/div[1]').click()
    driver.find_element(By.XPATH, '//*[@id="mobile_menu_collapse"]/div[1]/div[2]/a[3]').click()
    foto(driver, 'logoutMenuBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/login'

def test_profileSettingsMenuBTN():
    driver = webdriver.Chrome()
    driver.get("https://demo.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys('admin@example.com')
    driver.find_element(By.ID, 'password').send_keys('123456')
    driver.find_element(By.ID, 'submit-login').click()
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="dropdownMenuLink"]/div[1]').click()
    driver.find_element(By.XPATH, '//*[@id="mobile_menu_collapse"]/div[1]/div[2]/div/a').click()
    foto(driver, 'profileSettingsMenuBTN')
    assert driver.current_url == 'https://demo.worksuite.biz/account/settings/profile-settings'