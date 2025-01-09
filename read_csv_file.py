import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
import json

df=pd.read_csv("C:/Users/hrutu/Downloads/records.csv")
print(df)

with open('C:/Users/hrutu/Downloads/records.csv') as f:
    reader=csv.reader(f)
    data_read=[row for row in reader]

print(data_read)
print(type(data_read))

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

filtered_data=[]
missing=0

for i in range(0,len(data_read)):
    
    driver.get('https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=14281283799582374956&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9145648&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1')
    time.sleep(10)
    search_box = driver.find_element("xpath", '//input[@id="twotabsearchtextbox"]')

    search_box.send_keys(data_read[i][0])
    search_box.send_keys(Keys.ENTER)
    time.sleep(4)
    driver.execute_script('window.scroll(0,document.body.scrollHeight)')
    pages=int(driver.find_element(By.XPATH,'//span[@class="s-pagination-item s-pagination-disabled"]').text.strip())
    print(pages)
    for j in range(1,pages+1):
        url=f'https://www.amazon.in/s?k={data_read[i][0].strip()}&page={j}'
        driver.get(url)
        #product links elements
        products=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-line-clamp-2 s-link-style a-text-normal"]')
        links=[product.get_attribute('href') for product in products]
    
        for link in links:
            driver.get(link)
            time.sleep(2)
            try:
                name=driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]').text.strip()
                print(name)
                price=driver.find_element(By.XPATH,'//span[@class="a-price-whole"]').text.strip()
                brand=driver.find_element(By.XPATH,'//span[@class="a-size-base po-break-word"]').text.strip()

                filtered_data.append({
                        'Name':name,
                        'Price':price,
                        'Brand':brand
                })
            except Exception as e:
                missing+=1
        
    

print(filtered_data)

# csv
df=pd.DataFrame(filtered_data)
os.makedirs('output',exist_ok=True)
output_path='output/products3.csv'
df.to_csv(output_path,index=False)

# json
with open('C:/Users/hrutu/Desktop/Amazon web scraping using selenium/output/products3.json','w') as f:
    json.dump(filtered_data,f)


driver.close()
driver.quit()
