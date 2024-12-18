from selenium.webdriver.common.by import By
from utilities import XLUtils
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage():
    ddbtn_lang_xpath="//div[@class='d-flex justify-content-between align-items-center lang_custom_drpdown']"
    ddbtn_lang_xpath="//img[@class='ml-1 downIcon']"
    dd_engLang_xpath="//div[contains(text(),'EN')]"
    pic_profile_xpath="//div[@class='profile_thumbnail']"
    txt_prof_xpat="//div[@class='md-list-item-content md-ripple']//span[contains(text(),'Profile')]"

    txt_H_Kanban_x="//div[@class='col-xl-4 col-lg-6 order-lg-1']//p[@class='mb-0']" 
    txt_H_progress_x="//p[normalize-space()='Progress']"
    txt_progressTask_x="//p[normalize-space()='Task']"
    txt_progressMeeting_x="//p[normalize-space()='Meeting']"
    txt_progressRD_x="//p[normalize-space()='R&D']"
    dd_D_M_Y="//ul[@class='md-list md-theme-default']"
    txt_progressMonth_x="//ul[@class='md-list md-theme-default']//span[@class='md-list-item-text'][.='Month']"
    txt_progressWeek_x="//ul[@class='md-list md-theme-default']//span[@class='md-list-item-text'][.='Week']"
    txt_progressDay_x="//ul[@class='md-list md-theme-default']//span[@class='md-list-item-text'][.='Day']"
    txt_H_Calender_x="//p[@class='mb-0'][normalize-space()='Calendar']"
    txt_H_AT_x="//p[normalize-space()='Assigned Tasks']"
    txt_ATtask_x="//div[contains(text(),'Task')]"
    txt_ATspent_x="//div[contains(text(),'Est. / Spent')]"
    txt_ATduedate_x="//div[contains(text(),'Due Date')]"
    txt_ATstatus_x="//div[contains(text(),'Status')]"
    txt_ATeffort_x="//div[contains(text(),'Effort')]"

    path=r"C:\Users\NagalakshmiS\Desktop\pythonSelDemo.xlsx"

    def __init__(self,driver):
        self.driver=driver

    def click_language(self):
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.ddbtn_lang_xpath))).click()
        prof_pic=self.driver.find_element(By.XPATH, self.ddbtn_lang_xpath)
        self.driver.execute_script("arguments[0].click();", prof_pic)
        
    def click_english(self):
        prof_pic=self.driver.find_element(By.XPATH, self.dd_engLang_xpath)
        self.driver.execute_script("arguments[0].click();", prof_pic)
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.dd_engLang_xpath))).click()
        
    def click_prof_pic(self):
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.pic_profile_xpath))).click()
        prof_pic=self.driver.find_element(By.XPATH, self.pic_profile_xpath)
        self.driver.execute_script("arguments[0].click();", prof_pic)
        
    def click_prof_text(self):
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.txt_prof_xpat))).click()
        prof_btn=self.driver.find_element(By.XPATH, self.txt_prof_xpat)
        self.driver.execute_script("arguments[0].click();", prof_btn)
    
    def get_txt_H_Kanban_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_H_Kanban_x).text  
            
    def get_txt_H_progress_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_H_progress_x).text  
    def get_txt_progressTask_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_progressTask_x).text
    def get_txt_progressMeeting_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_progressMeeting_x).text
    def get_txt_progressRD_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_progressRD_x).text
    def get_txt_progressMonth_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_progressMonth_x).text
    def get_txt_progressWeek_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_progressWeek_x).text
    def get_txt_progressDay_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_progressDay_x).text
    
    def get_txt_H_Calender_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_H_Calender_x).text
        # ele=self.driver.find_element(By.XPATH, self.txt_H_Calender_x).text
        # print(ele.text)
        # here we can give only locator address instead of creating and calling a method.
    
    def get_txt_H_AT_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_H_AT_x).text
        print(text)
    def get_txt_ATtask_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_ATtask_x).text
    def get_txt_ATspent_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_ATspent_x).text
    def get_txt_ATduedate_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_ATduedate_x).text
    def get_txt_ATstatus_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_ATstatus_x).text
    def get_txt_ATeffort_x_name(self):
        return self.driver.find_element(By.XPATH, self.txt_ATeffort_x).text
    
    def run_in_test2(self):
        data1=XLUtils.readData(self.path,"DB_page",10,1) #to fetch 'kanban' for assertion with locator
        print(data1)
        if self.driver.find_element(By.XPATH, self.txt_H_Calender_x).text == data1:
            XLUtils.writeData(self.path,"DB_page",10,4,"pass")
            XLUtils.fillGreenColor(self.path,"DB_page",10,4)
            assert True
        else:
            XLUtils.writeData(self.path,"DB_page",10,4,"failed")
            XLUtils.fillRedColor(self.path,"DB_page",10,4)
            assert False 

    

        # XLUtils.load_excel(self.path,"DB_page")
        # data = XLUtils.get_data_as_list_tuples()
        # print(data)
        # for item in data:
        #     print(item[2])    #To print only 3rd col of data

        # self.rows=XLUtils.getRowCount(self.path, "DB_page") #to fetch entire first column data 
        # for r in range(2, self.rows):
        #     entire_colData= XLUtils.readData(self.path,"DB_page",r,1)
        #     print(entire_colData) 





   
    
    

    

