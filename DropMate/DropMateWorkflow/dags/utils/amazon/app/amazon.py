import undetected_chromedriver as uc 
import os 
import app.constants as const 
from undetected_chromedriver.patcher import Patcher
from app.utils import smart_find,smart_find_all
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



class Amazon(uc.Chrome): 
    def __init__(self, driver_path=r"C:\SeleniumDrivers",browser_path=r"C:\ChromeVersions\114\chrome.exe", teardown=True):
        self.driver_path = driver_path
        self.teardown = teardown
        self._quit_called = False 
        os.environ['PATH'] += self.driver_path
        super(Amazon,self).__init__(driver_executable_path=driver_path,browser_executable_path=browser_path) 
        self.implicitly_wait(const.DELAY)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.safe_quit()
    
    def __del__(self): 
        self.safe_quit()
        
    def safe_quit(self): 
        if not self._quit_called:
            try:
                super().quit()
            except Exception as e: 
                print(f"Safe quit failed: {e}")
            self._quit_called = True
    
    def land_first_page(self): 
        self.get(const.BASE_URL)
        
    def lookup(self, keywords, start_page=1, end_page=1, strict=True):
        """
        Scrapes Amazon search results for given keyword(s) from start_page to end_page.
        
        Returns:
            dict in format: {'page1': [url1, url2], 'page2': [...], ...}
        """ 
        
        search_query = '+'.join(keywords.split())
        results = {}
        
        for page_num in range(start_page, end_page + 1):
            url = url = const.BASE_URL + f"s?k={search_query}&i=fashion&rh=p_85%3A2470955011&page={page_num}"
            self.get(url)
        
            listings = smart_find_all(self,[
                (By.CSS_SELECTOR,'div[role="listitem"]')
            ],strict=strict) 
            listing1 = listings[0]
            link_el = listing1.find_element(By.XPATH, ".//a[contains(@href, '/dp/')]")
            href = link_el.get_attribute("href")

            if href:
                if href.startswith("/"):
                    href = "https://www.amazon.com" + href
            print(href)
            product_urls = [] 
            results[f"page{page_num}"] = listings
            print(f"Scraped {len(product_urls)} products from page {page_num}")

        return results
        # print(listings)
        # try: 
        #     title_element = smart_find(self, [
        #         (By.CSS_SELECTOR,'div[role="listitem"]'),
        #         (By.CSS_SELECTOR, 'h2[aria-label*="Real Leather Ratchet Dress Casual Belt, Cut to Exact Fit,Elegant Gift Box]"'),
        #         (By.ID,'dfb4c2c5-94e2-4101-b4df-dba72d8d5f87')
        #     ])
        # except TimeoutException:
        #     print("No product title found")
            
        
        
    @classmethod
    def from_patcher(cls, version=114, teardown=True, **kwargs):
        patched = Patcher(version_main=version)
        patched.auto()
        driver_path = patched.executable_path
        return cls(driver_path=driver_path,browser_path=rf"C:\ChromeVersions\{version}\chrome.exe",teardown=teardown, **kwargs)