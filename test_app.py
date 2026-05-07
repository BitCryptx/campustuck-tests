import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# WARNING: Yahan apne dost ke server ka asli IP aur port laazmi daalein!
APP_URL = "https://www.youtube.com" 

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Driver initialize karna
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_app_is_running(driver):
    """Test 1: Check karna ke website load ho rahi hai ya crash ho gayi"""
    driver.get(APP_URL)
    # Check karega ke title mein kuch na kuch likha ho (empty na ho)
    assert driver.title != "", "Website load nahi hui ya title khali hai!"

def test_page_load_time(driver):
    """Test 2: Check karna ke website 3 second ke andar load ho jati hai"""
    start_time = time.time()
    driver.get(APP_URL)
    load_time = time.time() - start_time
    assert load_time < 3.0, f"Website bohut slow hai! Load time: {load_time} seconds"

def test_main_content(driver):
    """Test 3: Check karna ke page ki body mein content (text) majood hai"""
    driver.get(APP_URL)
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert len(body_text) > 10, "Page par koi content nahi mil raha, shayad blank hai!"

def test_header_exists(driver):
    """Test 4: Check karna ke page par koi header ya navigation moojood hai"""
    driver.get(APP_URL)
    headers = driver.find_elements(By.TAG_NAME, "header")
    navs = driver.find_elements(By.TAG_NAME, "nav")
    assert len(headers) > 0 or len(navs) > 0, "Website par Header ya Navbar nahi mila!"