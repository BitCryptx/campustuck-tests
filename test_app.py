import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Deployment URL (Localhost Jenkins ke liye, aur IP bahar ke liye)
APP_URL = "http://localhost:5000" 

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Required for Jenkins/EC2
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

# --- 15 AUTOMATED TEST CASES ---

def test_1_page_title(driver):
    driver.get(APP_URL)
    assert "Campus Tuck" in driver.title

def test_2_logo_text(driver):
    driver.get(APP_URL)
    logo = driver.find_element(By.CLASS_NAME, "logo").text
    assert "Campus Tuck" in logo

def test_3_hero_heading(driver):
    driver.get(APP_URL)
    heading = driver.find_element(By.CSS_SELECTOR, ".hero-content h1").text
    assert "Your Campus Essentials Store" in heading

def test_4_shop_now_button_exists(driver):
    driver.get(APP_URL)
    btn = driver.find_element(By.CLASS_NAME, "hero-btn-primary")
    assert btn.is_displayed()

def test_5_find_us_button_exists(driver):
    driver.get(APP_URL)
    #for just testing purpose
    # Isliye hum check karenge ke element DOM mein mojood hai ya nahi
    btn = driver.find_elements(By.CLASS_NAME, "hero-btn-secondary")
    assert len(btn) > 0

def test_6_navbar_products_link(driver):
    driver.get(APP_URL)
    nav_links = driver.find_elements(By.CLASS_NAME, "nav-link")
    assert any("Products" in link.text for link in nav_links)

def test_7_user_login_button(driver):
    driver.get(APP_URL)
    btn = driver.find_element(By.CLASS_NAME, "btn-outline")
    assert "User Login" in btn.text

def test_8_admin_login_button(driver):
    driver.get(APP_URL)
    btn = driver.find_element(By.CLASS_NAME, "btn-solid")
    assert "Admin" in btn.text

def test_9_product_categories_heading(driver):
    driver.get(APP_URL)
    heading = driver.find_element(By.CSS_SELECTOR, ".section-title h2").text
    assert "Our Product Categories" in heading

def test_10_check_category_cards_count(driver):
    driver.get(APP_URL)
    cards = driver.find_elements(By.CLASS_NAME, "category-card")
    assert len(cards) >= 4  # Snacks, Beverages, Chocolate, Stationery

def test_11_footer_copyright(driver):
    driver.get(APP_URL)
    footer = driver.find_element(By.CLASS_NAME, "footer-bottom").text
    assert "2025 Campus Tuck" in footer

def test_12_social_links_count(driver):
    driver.get(APP_URL)
    links = driver.find_elements(By.CLASS_NAME, "social-link")
    assert len(links) == 4

def test_13_contact_info_phone(driver):
    driver.get(APP_URL)
    contact_section = driver.find_element(By.CLASS_NAME, "footer-contact").text
    assert "03151622934" in contact_section

def test_14_category_card_navigation(driver):
    driver.get(APP_URL)
    first_card = driver.find_element(By.CLASS_NAME, "category-card")
    link = first_card.get_attribute("href")
    assert "products.html" in link

def test_15_page_load_performance(driver):
    start_time = time.time()
    driver.get(APP_URL)
    end_time = time.time()
    assert (end_time - start_time) < 5  # Should load in less than 5 seconds