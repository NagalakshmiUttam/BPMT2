from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time
from pageobjects.dashboard_page import DashboardPage
from pageobjects.login_page import LoginPage
from  utilities import XLUtils
from selenium.webdriver.common.by import By

class TestEgDashboard:
    
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen() 

    email=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    # path=r"C:\Users\NagalakshmiS\Desktop\pythonSelDemo.xlsx"

    def test_dashboard(self, setup):
        self.logger.info("*** starting test_002_dashboard***")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp=LoginPage(self.driver)
        lp.setEmail(self.email)
        lp.setPW(self.password)
        lp.clickLogin()
        time.sleep(2)

        dp=DashboardPage(self.driver)
        dp.click_language()
        dp.click_english()

        abc=[]

        elements=self.driver.find_elements(By.XPATH, "//table/tbody/tr/th")
        for element in elements:
            print(element.text)
            # print(type(element))
            abc.append(element.text)
        print(abc)
            