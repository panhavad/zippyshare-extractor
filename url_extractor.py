from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
downloadable_urls=[]
in_urls_arr = []

def extractor(input_url):
    in_urls_arr = input_url.split("\n")
    print(in_urls_arr)

    for each_input_urls in in_urls_arr:
        driver.get(each_input_urls)
        try:
            download_link = driver.find_element(By.ID, 'dlbutton').get_attribute('href')
        except:
            print("An exception occurred")
        
        downloadable_urls.append(download_link)

    return "\n".join(downloadable_urls)
    