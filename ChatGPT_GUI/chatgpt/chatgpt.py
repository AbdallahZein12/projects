import chatgpt.constants as const   
import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class ChatGpt(uc.Chrome):
    def __init__(self,driver_path=r"C:\Selenium Drivers",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = uc.ChromeOptions()
        options.headless = False
        options.add_argument("--window-size=1880, 896")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        options.add_argument("--enable-javascript")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(ChatGpt,self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)
        
    def default_login(self,email,password):
        login_button = self.find_element(By.XPATH,'//button[div[text()="Log in"]]')
        login_button.click()
        email_entry = self.find_element(By.ID,"username")
        email_entry.clear()
        email_entry.send_keys(email)
        continue_button = self.find_element(By.XPATH,'//button[@type="submit" and text()="Continue"]')
        continue_button.click()
        try:
            email_message = self.find_element(By.ID,"error-element-username")
            email_error = "Invalid Email!"
            self.quit()
            return email_error
        except:
            print("Email successful")
            
        password_entry = self.find_element(By.ID,"password")
        password_entry.clear()
        password_entry.send_keys(password)
        continue_button = self.find_element(By.XPATH,'//button[@type="submit" and text()="Continue"]')
        continue_button.click()
        try:
            error_message = self.find_element(By.ID,"error-element-password")
            login_error = "Wrong email or password"
            self.quit()
            return login_error
        except:
            print("Login successful")
            successful_login = "Login successful"
            return successful_login
            
        
        
        
        
        
        
        
        