from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_rsi():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = None

    try:
        # 1. Chrome versiyasini qo'lda ko'rsatish
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(version="123.0.6312.123").install()),
            options=chrome_options
        )
        
        # 2. Sahifani ochish
        driver.get("https://www.tradingview.com/chart/")
        print("Sahifa ochildi")

        # 3. Indikatorlar menyusi
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='indicator-picker']"))
        ).click()
        print("Indikatorlar menyusi")

        # 4. RSI qidirish
        search = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-name='search-input']"))
        )
        search.send_keys("RSI")
        time.sleep(1)

        # 5. RSI tanlash
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Relative Strength Index')]"))
        ).click()
        print("RSI tanlandi")

        # 6. Qiymatni olish
        time.sleep(3)
        rsi_value = driver.find_element(By.XPATH, "//div[contains(@class, 'value-')]").text
        print(f"RSI: {rsi_value}")
        return rsi_value

    except Exception as e:
        print(f"Xato: {str(e)}")
        if driver:
            driver.save_screenshot('error.png')
        return None

    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    print("Natija:", get_rsi() or "Xatolik!")