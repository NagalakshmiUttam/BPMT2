import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import os
from datetime import datetime
from selenium.webdriver import ChromeOptions, Chrome

@pytest.fixture()
def setup(browser):
    # driver=webdriver.Chrome(ChromeDriverManager().install())
    # return driver
    if browser=='edge':
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Lunching Edge browser")
        return driver
    elif browser=='firefox':
        driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) #additional statement imported for this particular version
        print("Lunching firefox")
        return driver

    else:
        # driver=webdriver.Chrome(ChromeDriverManager().install())
        # print("Chrome browser is launching")
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = Chrome(options=opts)
        print("...Launching chrome browser...")
        driver.implicitly_wait(5)
        return driver
    

def pytest_addoption(parser): #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#It is a hook for Adding Environment info to HTML Report (we are commenting this because from now onwards we are using allure reports)
# def pytest_configure(config):
#     config._metadata['Project Name']='bpmt'
#     config._metadata['Module Name']='login_page'
#     config._metadata['Tester']='Nagalakshmi'

# #It is hook for delete/Modify Environment info to HTML Report

# # @pytest.mark.optionalhook
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

# #specifying the report folder location and save report with timestamp
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     #config.option.htmlpath=os.path.abspath(os.curdir)+"\\Reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
#     config.option.htmlpath=r"C:\\Nagalakshmi\\PythonPractice\\BPMT\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"