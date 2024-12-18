from pageobjects.employee_page import EmployeePage
from utilities.customLogger import LogGen
import time
from pageobjects.dashboard_page import DashboardPage
from utilities.common_login import CommonLogin

class TestEmployees:
    
    logger=LogGen.loggen() 

    def test_employees(self, setup):
        self.logger.info("*** starting test_03_employees***")
        self.driver=setup
        cmnlogin=CommonLogin(self.driver)
        cmnlogin.common_login()

        dp=DashboardPage(self.driver)
        dp.click_language()
        dp.click_english()
        dp.click_prof_pic()
        dp.click_prof_text()
        time.sleep(3)

        ep=EmployeePage(self.driver)
        # ep.set_profPic()
        # ep.click_editBtn()
        
        # ep.set_firstName("vandita")
        # ep.set_lastName("shetty")
        # ep.set_email("123sanil@gmail.com")
        # ep.set_mobileNum("99999999999")
        # ep.set_DOB("30.04.1999")
        # ep.set_bloodGrp("A+")
        # ep.set_empId("222")
        # ep.set_d_o_join("01.01.2020")
        # ep.set_address("Elephant gundi, MonkeyKadu, Mangalore-6666")

        # ep.click_ddButton1()
        # ep.click_department()

        # ep.click_ddButton2()
        # ep.click_role()
        
        # ep.click_ddButton3()
        # ep.click_designation()

        # ep.click_ddButton4()
        # ep.click_report_to()

        # ep.click_ddButton5()
        # ep.click_branch()

        # ep.click_updateBtn()
        ep.click_addSkill()
        time.sleep(2)

        ep.click_skillarrow()
        ep.click_addJava()
        ep.click_java_selector_rating()
        ep.click_addSymbol()
        
        ep.click_skillarrow()
        ep.click_addNet()
        ep.click_NetRating()
        ep.click_addSymbol()
       
        ep.click_skillarrow()
        ep.click_addC()
        ep.click_CRating()
        ep.click_addSymbol()
        
        ep.click_skillarrow()
        ep.click_addJavaScript()
        ep.click_JavaScriptRating()
        ep.click_addSymbol()
        
        ep.net8_test_color()
        ep.C5_test_color()
        ep.java4_test_color()
        ep.javaScript2_test_color()
        
        ep.click_1st_deleteSkill()
        ep.click_confirm_del()
        time.sleep(3)
        
        ep.click_2nd_deleteSkill()
        ep.click_confirm_del()
    
        ep.click_4th_deleteSkill()
        ep.click_confirm_del()
        time.sleep(2)

        ep.click_java_editRate10()
        time.sleep(2)
        ep.set_edit_confTxtbox("updated myself")
        time.sleep(2)
        ep.click_submitEdit()
        time.sleep(2)

        ep.click_3rd_deleteSkill()
        time.sleep(2)
        ep.click_confirm_del()
        # warning message will display to select the ratings.... here skills will be added in the alphabetical order
        self.logger.info("***End of the test_03_employees***")


    
    



