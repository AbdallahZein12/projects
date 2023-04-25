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
       return self.boxes_section_element.find_elements(By.CSS_SELECTOR,'div[data-testid="property-card"]')
   
    def pull_titles(self):
        time.sleep(5)
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').text
            hotel_name = hotel_name.encode('utf-16',errors='ignore')
            hotel_name = hotel_name.strip()
           
            # sys.stdout.buffer.write(hotel_name)
            
            hotel_price = deal_box.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]').text
            hotel_price = hotel_price.strip()
            
            
            hotel_score_box = deal_box.find_element(By.XPATH,'//div[contains(@aria-label, "Scored")]')
            hotel_score = hotel_score_box.text
            hotel_score = hotel_score.strip()
            
            collection.append([hotel_name,hotel_price,hotel_score])
        return collection
            
            