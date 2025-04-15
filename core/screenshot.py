from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def screenshot_site(url, output_path):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.save_screenshot(output_path)
    driver.quit()
