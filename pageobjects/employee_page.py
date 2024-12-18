from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color


class EmployeePage():
    prof_picUpload_xpath="//input[@type='file']"
    image_path = "C://Users//NagalakshmiS//Desktop//MicrosoftTeams-image.png"

    # btn_editProf_xpath="//div[@class='edit-button cursor-pointer']"
    # txt_firstName_xpath="//div[@class='modal-content']/descendant::div[contains(@class,'md-field')][1]/input[@type='text']"
    # txt_lastName_xpath="//div[@class='modal-content']/descendant::div[contains(@class,'md-field')][2]/input[@type='text']"
    # txt_email_xpath="//div[@class='modal-content']/descendant::div[contains(@class,'md-field')][3]/input[@type='text']"
    # txt_mobile_xpath="//div[@class='modal-content']/descendant::div[contains(@class,'md-field')][4]/input[@type='text']"
    # txt_DOB_xpath="//div[@class='modal-content']/descendant::div[contains(@class,'md-field')][5]/input[@type='text']"
    # txt_blood_grp_xpath="//div[@class='modal-content']/descendant::div[contains(@class,'md-field')][6]/input[@type='text']"
    # txt_empId_xpath="//div[@class='modal-content']/descendant::div[contains(@class,'md-field')][8]/input[@type='text']"
    # txt_d_o_join_xpath="//div[@class='modal-content']/descendant::div[contains(@class,'md-field')][9]/input[@type='text']"
    # txt_address_xpath="//div[@class='modal-content']/descendant::div[contains(@class,'md-field')][7]/textarea[@class='md-textarea']"

    # ddarrow1_xpath="//div[@id='departmentSelect']/descendant::div[@class='multiselect__select']"
    # dd_department_xpath="//div[@id='departmentSelect']/descendant::ul/li/span[.='Administration']"
    
    # ddarrow2_xpath="//div[@class='multiselect multiselect--above']/child::div[@class='multiselect__select']"
    # dd_role_xpath="//div[@id='roleSelect']/descendant::ul/li/span[.='Admin']"

    # ddarrow3_xpath="//div[@id='designationSelect']/descendant::div[@class='multiselect__select']"
    # dd_designation_xpath="//div[@id='designationSelect']/descendant::ul/li/span[.='Admin Manager']"

    # ddarrow4_xpath="//div[@id='reportingSelect']/descendant::div[@class='multiselect__select']"
    # dd_report_to_xpath="//div[@id='reportingSelect']/descendant::ul/li/span[.='Vittaldas Bhat']"

    # ddarrow5_xpath="//div[@id='branchSelect']//div[@class='multiselect__select']"
    # dd_branch_xpath="//div[@id='branchSelect']//ul/li/span[.='Canada']"

    # btn_update_xpath="//footer[@class='modal-footer']//div[.='Update']"

    img_addSkill_xpath="//img[@class='add-skill_icon']"
    dd_skillarrow_xpath="//div[@id='skillId']//div[@class='multiselect__select']"
    dd_addJava_xpath="//div[@id='skillId']//ul/li/span[.='Java']"
    java_selector_rating_xpath="//div[@class='rating-selector']//input[@id='RelationalDb-4']"
    img_plusSymbol_xpath="//button[@class='btn no-outline']//img"

    dd_addNet_xpath="//div[@id='skillId']//ul/li/span[.='A# .NET']"
    net_selector_rating_xpath="//div[@class='rating-selector']//input[@id='RelationalDb-8']"

    dd_addC_xpath="//div[@id='skillId']//ul/li/span[.='C']"
    C_selector_rating_xpath="//div[@class='rating-selector']//input[@id='RelationalDb-5']"

    dd_addJavaScript_xpath="//div[@id='skillId']//ul/li/span[.='JavaScript']"
    JS_selector_rating_xpath="//div[@class='rating-selector']//input[@id='RelationalDb-2']"

    btn_delete_first_xpath="//table[contains(@class,'table')]//tbody/tr[2]/td//button[@type='button']"
    btn_delete_second_xpath="//table[contains(@class,'table')]/tbody/tr[2]//p[.='C']/../following-sibling::td[2]/button"
    btn_delete_third_xpath="//table[contains(@class,'table')]/tbody/tr[2]//p[.='Java']/../following-sibling::td[2]/button"
    btn_delete_fourth_xpath="//table[contains(@class,'table')]/tbody/tr[3]//p[.='JavaScript']/../following-sibling::td[2]/button"
    btn_del_dialogbox_xpath="//div[@class='modal-content']//div[.='Delete']"

    edit_java_selectorRate_xpath="//tbody/tr[2]/td[2]/div/div/label[@class='warning_rating'][10]"
    edit_confTxtbox_xpath="(//div[contains(@id,'skill')])[4]/descendant::input[@class='md-input'] [@id='user_reason']"

    # edit_popup="//h2[normalize-space()='Edit Skills']"
    btn_submitEdit_xpath = "//div[contains(text(),'Submit')]"
    # cancel_button = "//div[contains(text(),'Cancel')]"

    def __init__(self,driver):
        self.driver=driver

    def set_profPic(self):
        self.driver.find_element(By.XPATH,self.prof_picUpload_xpath).send_keys(self.image_path)
                                                                               
    # def click_editBtn(self):
    #     clickEdit=self.driver.find_element(By.XPATH,self.btn_editProf_xpath)
    #     self.driver.execute_script("arguments[0].click();", clickEdit)
    
    # def set_firstName(self, F_name):
    #     self.driver.find_element(By.XPATH, self.txt_firstName_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_firstName_xpath).send_keys(F_name)
    
    # def set_lastName(self, L_name):
    #     self.driver.find_element(By.XPATH, self.txt_lastName_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_lastName_xpath).send_keys(L_name)

    # def set_mobileNum(self, M_MobileNum):
    #     self.driver.find_element(By.XPATH, self.txt_mobile_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_mobile_xpath).send_keys(M_MobileNum)

    # def set_email(self, E_email):
    #     self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(E_email)

    # def set_DOB(self, DOB):
    #     self.driver.find_element(By.XPATH, self.txt_DOB_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(DOB)

    # def set_bloodGrp(self, bloodGrp):
    #     self.driver.find_element(By.XPATH, self.txt_blood_grp_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_blood_grp_xpath).send_keys(bloodGrp)

    # def set_empId(self, empId):
    #     self.driver.find_element(By.XPATH, self.txt_empId_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_empId_xpath).send_keys(empId)

    # def set_d_o_join(self, d_o_join):
    #     self.driver.find_element(By.XPATH, self.txt_d_o_join_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_d_o_join_xpath).send_keys(d_o_join)
    
    # def set_address(self, address):
    #     self.driver.find_element(By.XPATH, self.txt_address_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txt_address_xpath).send_keys(address)

    # def click_ddButton1(self):
    #     self.driver.find_element(By.XPATH, self.ddarrow1_xpath).click()
    # def click_department(self):
    #     dept= self.driver.find_element(By.XPATH, self.dd_department_xpath)
    #     self.driver.execute_script("arguments[0].click();", dept)
        
    # def click_ddButton2(self):
    #     role_btn=self.driver.find_element(By.XPATH, self.ddarrow2_xpath)
    #     self.driver.execute_script("arguments[0].click();", role_btn)
    # def click_role(self):
    #     role=self.driver.find_element(By.XPATH, self.dd_role_xpath)
    #     self.driver.execute_script("arguments[0].click();", role)

    # def click_ddButton3(self):
    #     designation_btn=self.driver.find_element(By.XPATH, self.ddarrow3_xpath)
    #     self.driver.execute_script("arguments[0].click();", designation_btn)
    # def click_designation(self):
    #     designation=self.driver.find_element(By.XPATH, self.dd_designation_xpath)
    #     self.driver.execute_script("arguments[0].click();", designation)

    # def click_ddButton4(self):
    #     reporting_btn=self.driver.find_element(By.XPATH, self.ddarrow4_xpath)
    #     self.driver.execute_script("arguments[0].click();", reporting_btn)
    # def click_report_to(self):
    #     report_to=self.driver.find_element(By.XPATH, self.dd_report_to_xpath)
    #     self.driver.execute_script("arguments[0].click();", report_to)

    # def click_ddButton5(self):
    #     branch_btn=self.driver.find_element(By.XPATH, self.ddarrow5_xpath)
    #     self.driver.execute_script("arguments[0].click();", branch_btn)
    # def click_branch(self):
    #     branch=self.driver.find_element(By.XPATH, self.dd_branch_xpath)
    #     self.driver.execute_script("arguments[0].click();", branch)

    # def click_updateBtn(self):
    #     updateBtn=self.driver.find_element(By.XPATH, self.btn_update_xpath)
    #     self.driver.execute_script("arguments[0].click();", updateBtn)

    def click_addSkill(self):
        addSkill=self.driver.find_element(By.XPATH, self.img_addSkill_xpath)
        self.driver.execute_script("arguments[0].click();", addSkill)
       
    def click_skillarrow(self):
        skillarrow=self.driver.find_element(By.XPATH, self.dd_skillarrow_xpath)
        self.driver.execute_script("arguments[0].click();", skillarrow)
    def click_addJava(self):
        addJava=self.driver.find_element(By.XPATH, self.dd_addJava_xpath)
        self.driver.execute_script("arguments[0].click();", addJava)
    def click_java_selector_rating(self):
        java_selector_rating=self.driver.find_element(By.XPATH, self.java_selector_rating_xpath)
        self.driver.execute_script("arguments[0].click();", java_selector_rating)
    def click_addSymbol(self):
        addSymbol=self.driver.find_element(By.XPATH, self.img_plusSymbol_xpath)
        self.driver.execute_script("arguments[0].click();", addSymbol)

    
    def click_addNet(self):
        addNet=self.driver.find_element(By.XPATH, self.dd_addNet_xpath)
        self.driver.execute_script("arguments[0].click();", addNet)
    def click_NetRating(self):
        netRating=self.driver.find_element(By.XPATH, self.net_selector_rating_xpath)
        self.driver.execute_script("arguments[0].click();", netRating) 

    def click_addC(self):
        addC=self.driver.find_element(By.XPATH, self.dd_addC_xpath)
        self.driver.execute_script("arguments[0].click();", addC)
    def click_CRating(self):
        cRating=self.driver.find_element(By.XPATH, self.C_selector_rating_xpath)
        self.driver.execute_script("arguments[0].click();", cRating)

    def click_addJavaScript(self):
        addJavaScript=self.driver.find_element(By.XPATH, self.dd_addJavaScript_xpath)
        self.driver.execute_script("arguments[0].click();", addJavaScript)
    def click_JavaScriptRating(self):
        javaScriptRating=self.driver.find_element(By.XPATH, self.JS_selector_rating_xpath)
        self.driver.execute_script("arguments[0].click();", javaScriptRating)


    def click_1st_deleteSkill(self):
        deleteNet=self.driver.find_element(By.XPATH, self.btn_delete_first_xpath)
        self.driver.execute_script("arguments[0].click();", deleteNet)

    def click_2nd_deleteSkill(self):
        deleteC=self.driver.find_element(By.XPATH, self.btn_delete_second_xpath)
        self.driver.execute_script("arguments[0].click();", deleteC)

    def click_3rd_deleteSkill(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,self.btn_delete_third_xpath)))
        # deletejava=self.driver.find_element(By.XPATH, self.btn_delete_third_xpath)
        # deletejava.click()
        deletejava=self.driver.find_element(By.XPATH, self.btn_delete_third_xpath)
        self.driver.execute_script("arguments[0].click();", deletejava)
       
    def click_4th_deleteSkill(self):
        deleteJS=self.driver.find_element(By.XPATH, self.btn_delete_fourth_xpath)
        self.driver.execute_script("arguments[0].click();", deleteJS)
        
    def click_confirm_del(self):
        confirm_del=self.driver.find_element(By.XPATH, self.btn_del_dialogbox_xpath)
        self.driver.execute_script("arguments[0].click();", confirm_del)

    def click_java_editRate10(self):
        java_editRate10=self.driver.find_element(By.XPATH, self.edit_java_selectorRate_xpath)
        self.driver.execute_script("arguments[0].click();", java_editRate10)

    def set_edit_confTxtbox(self, reason):
        self.driver.find_element(By.XPATH, self.edit_confTxtbox_xpath).send_keys(reason)
    
    def click_submitEdit(self):
        submitEdit=self.driver.find_element(By.XPATH, self.btn_submitEdit_xpath)
        self.driver.execute_script("arguments[0].click();", submitEdit)

    def net8_test_color(self):
        color1=Color.from_string(self.driver.find_element(By.XPATH,"//tbody/tr[2]//p[.='A# .NET']/../following-sibling::td//label[@class='success_rating'][8]").value_of_css_property('background-color'))
        print("green==>", color1)
        assert color1.rgba == 'rgba(165, 196, 77, 0.3)'
    
    def C5_test_color(self):
        color2=Color.from_string(self.driver.find_element(By.XPATH,"//tbody/tr[3]//p[.='C']/../following-sibling::td//label[@class='warning_rating'][5]").value_of_css_property('background-color'))
        print("orange==>", color2)

    def java4_test_color(self):
        color3=Color.from_string(self.driver.find_element(By.XPATH,"//tbody/tr[4]//p[.='Java']/../following-sibling::td//label[@class='warning_rating'][4]").value_of_css_property('background-color'))
        print("orange again==>",color3)
        print(type(color3))
        assert color3.rgba == 'rgba(255, 193, 7, 0.3)'

    def javaScript2_test_color(self):
        color4=Color.from_string(self.driver.find_element(By.XPATH,"//tbody/tr[5]//p[.='JavaScript']/../following-sibling::td//label[@class='error_rating'][2]").value_of_css_property('background-color'))
        print("red==>", color4)
        print(type(color4))
        if color4.rgba =='rgba(255, 119, 106, 0.3)':
            assert True
        else:
            assert False

        
    


        

    

    
    


    
        
        
    
    
        
        



