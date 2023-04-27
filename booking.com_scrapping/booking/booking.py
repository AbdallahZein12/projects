import booking.constants as const
import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import time
from booking.booking_filtration import BookingFiltration
from selenium.webdriver.common.keys import Keys
from booking.booking_report import BookingReport
from prettytable import PrettyTable
from booking import loading as loading
import threading



class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Selenium Drivers",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--window-size=1880, 896")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        options.add_argument("--enable-javascript")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking,self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()
        
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)
        
    def change_currency(self,currency=None):
        
        
        try:
            close_login_popup = self.find_element(By.CSS_SELECTOR,'button[aria-label="Dismiss sign-in info."]')
            close_login_popup.click()
        except:
            print("Could not find login popup, skipping...")
            
        currency_element = self.find_element(By.CSS_SELECTOR,'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        
        currency_span_element = self.find_element(By.XPATH,f"//span[@class='cf67405157' and contains(text(), '{currency}')]")
        button_elem = currency_span_element.find_element(By.XPATH,"./ancestor::button[contains(@class,'fc63351294')]")
        button_elem.click()
        
    def select_place_to_go(self,place_to_go):
        search_field = self.find_element(By.ID,":Ra9:")
        search_field.clear()
        search_field.send_keys(place_to_go)
        
        first_result = self.find_element(By.CSS_SELECTOR,'ul[data-testid="autocomplete-results"] li:first-child')
        first_result.click()
        
      
        
    def select_dates(self,check_in_date,check_out_date):
        
        split_check_in_date = check_in_date.split(" ")
        in_year = split_check_in_date[2]
        in_month = split_check_in_date[1]
        
        split_check_out_date = check_out_date.split(" ")
        out_year = split_check_out_date[2]
        out_month = split_check_out_date[1]
        
        counter = True
        while True:
            calendar_box = self.find_element(By.CLASS_NAME,"fa3f76ae6b")
            website_year_and_month1 = calendar_box.find_element(By.CSS_SELECTOR,'h3[aria-live="polite"]')
                
            
                
            
            website_year_and_month1_text = website_year_and_month1.text
            split_website_year_and_month1 = website_year_and_month1_text.split(" ")
            month1 = split_website_year_and_month1[0]
            year1 = split_website_year_and_month1[1]
            
            website_year_and_month2 = calendar_box.find_elements(By.CSS_SELECTOR,'h3[aria-live="polite"]')
            website_year_and_month2 = website_year_and_month2[1]
            website_year_and_month2_text = website_year_and_month2.text
            split_website_year_and_month2 = website_year_and_month2_text.split(" ")
            month2 = split_website_year_and_month2[0]
            year2 = split_website_year_and_month2[1]
            
            bigger_calendar_box = self.find_element(By.CSS_SELECTOR,'div[data-testid="searchbox-datepicker-calendar"]')
            if (in_month != month1 or in_year != year1) and (in_month != month2 or in_year != year2):
                if counter:
                    calendar_arrow = bigger_calendar_box.find_element(By.CSS_SELECTOR,'button[type="button"]')
                    counter = False
                    continue
                else:
                    calendar_arrow = bigger_calendar_box.find_elements(By.CSS_SELECTOR,'button[type="button"]')
                    # print(calendar_arrow)
                    try:
                        calendar_arrow = calendar_arrow[1]
                    except:
                        calendar_arrow = calendar_arrow[0]
                    calendar_arrow.click()
                    continue
            else:
                check_in_element = self.find_element(By.CSS_SELECTOR,f'span[aria-label="{check_in_date}"]')
                check_in_element.click()
                # calendar_arrow = bigger_calendar_box.find_element(By.CSS_SELECTOR,'button[type="button"]')
                # counter = True
                break
            
        while True:
            calendar_box = self.find_element(By.CLASS_NAME,"fa3f76ae6b")
            website_year_and_month1 = calendar_box.find_element(By.CSS_SELECTOR,'h3[aria-live="polite"]')
                
            
                
            
            website_year_and_month1_text = website_year_and_month1.text
            split_website_year_and_month1 = website_year_and_month1_text.split(" ")
            month1 = split_website_year_and_month1[0]
            year1 = split_website_year_and_month1[1]
            
            website_year_and_month2 = calendar_box.find_elements(By.CSS_SELECTOR,'h3[aria-live="polite"]')
            website_year_and_month2 = website_year_and_month2[1]
            website_year_and_month2_text = website_year_and_month2.text
            split_website_year_and_month2 = website_year_and_month2_text.split(" ")
            month2 = split_website_year_and_month2[0]
            year2 = split_website_year_and_month2[1]
            
            if (out_month != month1 or out_year != year1) and (out_month != month2 or out_year != year2):
                if counter:
                    calendar_arrow = bigger_calendar_box.find_element(By.CSS_SELECTOR,'button[type="button"]')
                    calendar_arrow.click()
                    counter = False
                    continue
                else:
                    calendar_arrow = bigger_calendar_box.find_elements(By.CSS_SELECTOR,'button[type="button"]')
                    try:
                        calendar_arrow = calendar_arrow[1]
                    except:
                        calendar_arrow = calendar_arrow[0]
                    calendar_arrow.click()
                    continue
                    
            else:
                check_in_element = self.find_element(By.CSS_SELECTOR,f'span[aria-label="{check_out_date}"]')
                check_in_element.click()
                break
            
    def select_adults(self, adults=1,children=0,ages=[],rooms=1):
        selection_element = self.find_element(By.CSS_SELECTOR,'button[data-testid="occupancy-config"]')
        selection_element.click()
        
        while True:
            occupancy_popup = self.find_element(By.CSS_SELECTOR,'div[data-testid="occupancy-popup"]')
            buttons = occupancy_popup.find_elements(By.CSS_SELECTOR,'button[tabindex="-1"]')
            boxes = occupancy_popup.find_elements(By.CLASS_NAME,"e98c626f34")
            
            
            decrease_adult_num = buttons[0]
            adult_num_box = boxes[0]
            default_adult_number = adult_num_box.find_element(By.CLASS_NAME,"e615eb5e43")
            
            if default_adult_number.text != "1":
                # print(f"Def Adul Num: {default_adult_number.text}")
                decrease_adult_num.click()
                continue
            
            decrease_children_num = buttons[2]
            default_children_number_box = boxes[1]
            default_children_number = default_children_number_box.find_element(By.CLASS_NAME,"e615eb5e43")
            
            if default_children_number.text != "0":
                # print(f"Def Child Num: {default_children_number.text}")
                decrease_children_num.click()
                continue
            
            decrease_room_num = buttons[4]
            default_room_num_box = boxes[2]
            default_room_num = default_room_num_box.find_element(By.CLASS_NAME,"e615eb5e43")
            
            
            if default_room_num.text != "1":
                # print(f"Def Room Num: {default_room_num.text}")
                decrease_room_num.click()
                continue
            
            break
        
        
        while True:
            occupancy_popup = self.find_element(By.CSS_SELECTOR,'div[data-testid="occupancy-popup"]')
            buttons = occupancy_popup.find_elements(By.CSS_SELECTOR,'button[tabindex="-1"]')
            boxes = occupancy_popup.find_elements(By.CLASS_NAME,"e98c626f34")
            
            
            adult_num_box = boxes[0]
            default_adult_number = adult_num_box.find_element(By.CLASS_NAME,"e615eb5e43")
            default_children_number_box = boxes[1]
            default_children_number = default_children_number_box.find_element(By.CLASS_NAME,"e615eb5e43")
            default_room_num_box = boxes[2]
            default_room_num = default_room_num_box.find_element(By.CLASS_NAME,"e615eb5e43")
            default_room_num_text = default_room_num.text
            
            
            if default_adult_number.text != str(adults):
                increase_adults = buttons[1]
                increase_adults.click()
                continue
            if default_children_number.text != str(children):
                increase_children = buttons[3]
                increase_children.click()
                continue
            
            if len(ages) > 0: 
                count = 0
                for x in (ages):
                    list_of_ages_needed = [i.get_attribute("id") for i in self.find_elements(By.NAME,"age")]
                    select_element = self.find_element(By.ID,list_of_ages_needed[count])
                    option_element = select_element.find_element(By.CSS_SELECTOR,f"option[value='{x}']")
                    option_element.click() 
                    reset_button = self.find_element(By.CSS_SELECTOR,'button[data-testid="occupancy-config"]')
                    reset_button.click()
                    count+=1
                   
            
            if default_room_num_text != str(rooms):
                
                if children > 0:
                    increase_rooms_buttons = WebDriverWait(self,10).until(ec.visibility_of_element_located((By.XPATH,'//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[5]/div[2]/button[2]')))
                else:
                    increase_rooms_buttons = WebDriverWait(self,10).until(ec.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div/div/form/div[1]/div[3]/div/div/div/div/div[3]/div[2]/button[2]')))
                increase_rooms_buttons.click()
                continue
            break
    def click_search(self):
        submit_button = self.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        submit_button.click()
        
    def apply_filtration(self):
        print("\033[?25l")
        # self.execute_script("document.body.style.zoom='75%'")
        
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating("5 stars","4 stars")
        # try:
        #     filtration.apply_star_rating("5 stars")
        # except:
        #     filtration.apply_star_rating("4 stars")
        filtration.sort_price_lowest_first()
        
        
    def report_results(self):
        
        stop_event = threading.Event()
        t = threading.Thread(target=loading.run,args=(stop_event,),daemon=True)
        t.start()
        
        hotel_boxes = self.find_element(By.CLASS_NAME,'d4924c9e74')
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        
        table.add_rows(report.pull_titles(stop_event))
        t.join()
        print(table)
        
       
                
            
            
            
                
            
            
                    
            
    
            
        
            
        