
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest
import time
from pageobjects.dashboard_page import DashboardPage
from pageobjects.login_page import LoginPage
from  utilities import XLUtils
from utilities.common_login import CommonLogin


class TestDashboard:

    def test_dashboard(self,setup):
        logger=LogGen.loggen() 
        logger.info("*** starting test_002_dashboard***")
        
        self.driver=setup
        cmnlogin=CommonLogin(self.driver)
        cmnlogin.common_login()
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()

    #     lp=LoginPage(self.driver)
    #     lp.setEmail(self.email)
    #     lp.setPW(self.password)
    #     lp.clickLogin()
    #     time.sleep(10)

        dp=DashboardPage(self.driver)
        dp.click_language()
        dp.click_english()
        dp.click_prof_pic()
        dp.click_prof_text()

        dp.run_in_test2()
        
        logger.info("***End of the test_002_dashboard***")