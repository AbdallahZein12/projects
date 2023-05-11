#Includes class with instance methods
#Responsible to interact with website filteration

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

class BookingFiltration:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        try:
            map_popup_button = self.driver.find_element(By.CLASS_NAME,"map_full_overlay__close")
            map_popup_button.click()
        except:
            print("Could not find map popup, skipping...")
            print()
    def apply_star_rating(self,*star_values):
        self.driver.execute_script("window.scrollBy(0, 750)")
        
        try:
            star_filteration_box = self.driver.find_element(By.ID,"filter_group_class_:Rsq:")
        except:
            try:
                star_filteration_box = self.driver.find_element(By.ID,"filter_group_class_:R14q:")
            except:
                star_filteration_box = self.driver.find_element(By.ID,"filter_group_class_:R1cq:")
        star_child_element = star_filteration_box.find_elements(By.CSS_SELECTOR,'*')
        for star_value in star_values:
            for star_element in star_child_element:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value}':
                    star_element.click()
                    break
                    
                elif str(star_element.get_attribute('innerHTML')).strip() == str(star_child_element[-1].get_attribute('innerHTML')).strip():
                    if str(star_element.get_attribute('innerHTMl')).strip() == f'{star_value}':
                        star_element.click()
                    else:
                        star_value_num = star_value.split(" ")
                        try:
                            star_value = str(int(star_value_num[0])-1) + " stars"
                            star_element = star_filteration_box.find_element(By.XPATH,f"//*[contains(text(),'{star_value}')]")
                            star_element.click()
                        except:
                            try:
                                star_value = str(int(star_value_num[0])-2) + " stars"
                                star_element = star_filteration_box.find_element(By.XPATH,f"//*[contains(text(),'{star_value}')]")
                                star_element.click()
                            except:
                                star_value = str(int(star_value_num[0])-3) + " stars"
                                star_element = star_filteration_box.find_element(By.XPATH,f"//*[contains(text(),'{star_value}')]")
                                star_element.click()
     
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, 0)")
        
    def sort_price_lowest_first(self):
        sorting_box = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        sorting_box.click()
        
        sorting_drop_down_menu = self.driver.find_element(By.CSS_SELECTOR,'div[data-testid="sorters-dropdown"]')
        price_lowest = sorting_drop_down_menu.find_element(By.CSS_SELECTOR,'button[data-id="price"]')
        price_lowest.click()
                
      