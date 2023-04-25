#Includes methods that will parse specific data I need from each one of the deal boxes
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import sys
import time


class BookingReport:
    def __init__(self,boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()
        
    def pull_deal_boxes(self):
        all_elements_in_box = self.boxes_section_element.find_elements(By.XPATH,".//*")
        deal_boxes = []
        # deal_boxes = [i for i in all_elements_in_box if i.get_attribute("data-testid") == "property-card" or i.get_attribute("data-testid") == "sticky-container"]
    
        for i in all_elements_in_box:
            if i.get_attribute("data-testid") == "property-card":
                deal_boxes.append(i)
            elif i.get_attribute("data-testid") == "sticky-container":
                break
            else:
                pass
                
        return deal_boxes
        
        
    def pull_titles(self):
        time.sleep(5)
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').get_attribute('innerHTML')
            hotel_name = hotel_name.strip()
            
            # sys.stdout.buffer.write(hotel_name)    
            
            hotel_price = deal_box.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]').text
            hotel_price = hotel_price.strip()
            
            
            hotel_score_box = deal_box.find_element(By.XPATH,'//div[contains(@aria-label, "Scored")]')
            hotel_score = hotel_score_box.text
            hotel_score = hotel_score.strip()
            
            collection.append([hotel_name,hotel_price,hotel_score])
        return collection
            
            