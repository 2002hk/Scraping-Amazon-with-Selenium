from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Step 1: Go to Google and Search "Ajio Men Grooming"
driver.get("https://www.google.com/")
time.sleep(2)

# Locate the Google Search Box and Enter the Query
search_box = driver.find_element("xpath", '//*[@id="APjFqb"]')
search_box.send_keys("amazon pendrive")
search_box.send_keys(Keys.ENTER)
time.sleep(3)
# this finds the first link and clicks on it
driver.find_element(By.XPATH,'//a[@class="sVXRqc"]').click()
time.sleep(3)
#scrolling to the last
driver.execute_script('window.scroll(0,document.body.scrollHeight)')
time.sleep(2)

# fetching total number of pages
pages=int(driver.find_element(By.XPATH,'//span[@class="s-pagination-item s-pagination-disabled"]').text.strip())
print(pages)
filtered_data=[]
for i in range(1,pages+1):
    url=f'https://www.amazon.in/s?k=pendrive&page={i}'
    driver.get(url)
    products=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-line-clamp-2 s-link-style a-text-normal"]')
    # Extract the 'href' attribute from each WebElement
    links = [product.get_attribute('href') for product in products]

    
    for link in links:
        driver.get(link)
        time.sleep(3)
        name=driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]').text.strip()
        price=driver.find_element(By.XPATH,'//span[@class="a-price-whole"]').text.strip()
        brand=driver.find_element(By.XPATH,'//span[@class="a-size-base po-break-word"]').text.strip()
        filtered_data.append({
            'Name':name,
            'Price':price,
            'Brand':brand
        })
        
print(filtered_data)
print(f"No of scraped products{len(filtered_data)}")
df=pd.DataFrame(filtered_data)
os.makedirs('output',exist_ok=True)
output_path='output/products.csv'
df.to_csv(output_path,index=False)
driver.close()
driver.quit()