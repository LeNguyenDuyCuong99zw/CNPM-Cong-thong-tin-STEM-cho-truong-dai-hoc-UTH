import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#inherit TestCase Class and create a new test class 
user="ADMIN"
access_key="12345"
class PythonOrgSearch(unittest.TestCase):
    #initialization of webdriver
    def setUp(self):
        
        self.driver = webdriver.Chrome()
    #self.driver = webdriver.Remote(
    #    command_executor='http://127.0.0.1:8000/admin/login/?next=/admin/',
    #    desired_capabilities=desired_caps)
    #Test case method. It should always start with test_ 
    def TEST_LOGIN(self):
        #get driver
        print("bat dau")
        driver = self.driver
        #get python.org using selenium
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        inputUsername = driver.find_element(By.NAME,value="username")
        print(inputUsername)
        inputUsername.send_keys("admin")
        time.sleep(5)

        password = driver.find_element(By.NAME,value="password")
        print(inputUsername)
        password.send_keys("07012005")
        time.sleep(5)

        password.send_keys(Keys.RETURN)
        print("111111111")
        #receive data 
        #elem.send_key(Keys.RETURN)
        #assert "No results found." not in driver.page_source


        #clean up method called after every test performed

        #TH1 nhập username đúng nhưng password sai ---> Kết quả kỳ vọng: không thể đăng nhập
        #TH2 nhập username sai và password đúng ----> không thể đăng nhập
        #TH3 nhập username và password đúng ----> đăng nhập thành công----->vào trang hệ thống
        #Không nhập gì hết ----> không thể đăng nhập
    def tearDown(self):
            self.driver.close()
    def test_unit_user_should_able_to_add_item(self):
            #try:
            #get driver
            print("bat dau")
            driver = self.driver
            #get python.org using selenium
            driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
            inputUsername = driver.find_element(By.NAME,value="username")
            


            inputUsername.send_keys("admin")
            #time.sleep(5)
            password = driver.find_element(By.NAME,value="password")

            password.send_keys("07012005")
            #time.sleep(5)
            password.send_keys(Keys.RETURN)    
            time.sleep(10)
            actualTitle = driver.title
            print(actualTitle)
            assert actualTitle == "Site administration | Django site admin"
            #assert actualTitle == "Site administration | Django site admin"
            #assert 2 + 2 == 5 "Houston we have a problem"


            #receive data
            #elem.send_key(Keys.RETURN)
            #assert "No results found." not in driver.page_source
    #execute the script
            
                                
if __name__ == "__main__":
    unittest.main()
