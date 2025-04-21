import undetected_chromedriver as uc 
import os 
import app.constants as const 
from undetected_chromedriver.patcher import Patcher



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
        
    @classmethod
    def from_patcher(cls, version=114, teardown=True, **kwargs):
        patched = Patcher(version_main=version)
        patched.auto()
        driver_path = patched.executable_path
        return cls(driver_path=driver_path,browser_path=rf"C:\ChromeVersions\{version}\chrome.exe",teardown=teardown, **kwargs)