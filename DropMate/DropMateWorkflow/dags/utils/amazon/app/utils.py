from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def smart_find(driver, strategies, timeout=5):
    """
    Tries multiple locator strategies with optional timeout.
    
    strategies: List of (By.TYPE, "value") tuples
    Example:
        [
            (By.ID, "productTitle"),
            (By.XPATH, "//span[@id='productTitle']"),
            (By.CSS_SELECTOR, "#productTitle")
        ]
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        for by, value in strategies:
            try:
                return driver.find_element(by, value)
            except NoSuchElementException:
                continue
        time.sleep(0.2)  
    raise TimeoutException(f"Element not found after {timeout}s using strategies: {strategies}")

def smart_find_all(driver, strategies, timeout=5,strict=True):
    """
    Tries multiple locator strategies until elements are found or timeout is hit.

    Params:
        driver     : Selenium/UC driver
        strategies : list of (By, value) tuples
        timeout    : max wait time in seconds
        strict     : if True, raises TimeoutException on failure

    Returns:
        List of elements, or empty list if not strict
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        for by, value in strategies:
            try:
                elements = driver.find_elements(by, value)
                if elements:
                    print(f"Found elements using: {by} = {value}")
                    return elements
            except Exception:
                continue
        time.sleep(0.2)
    if strict:
        raise TimeoutException(f"smar_find_all: No elements found with any strategy in {timeout}s.")
    else:
        print("smart_find_all: WARNING! No elements found, returning empty list")
    return []
