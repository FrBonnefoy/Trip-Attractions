from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ProcessPoolExecutor

from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor, as_completed

import tqdm
chrome_options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument("--window-size=1366x4000")
chrome_options.add_argument('--headless')
chrome_options.add_argument('start-maximized')
#browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
'''
"'https://www.tripadvisor.fr/Attractions-g187208-Activities-c61-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c42-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c47-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c26-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c55-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c57-Provence_Alpes_Cote_d_Azur.html','https://www.tripadvisor.fr/Attractions-g187208-Activities-c36-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c49-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c56-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c40-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c59-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c20-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c41-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c60-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c58-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c52-Provence_Alpes_Cote_d_Azur.html','https://www.tripadvisor.fr/Attractions-g187208-Activities-c53-Provence_Alpes_Cote_d_Azur.html, https://www.tripadvisor.fr/Attractions-g187208-Activities-c48-Provence_Alpes_Cote_d_Azur.html, 'https://www.tripadvisor.fr/Attractions-g187208-Activities-c62-Provence_Alpes_Cote_d_Azur.html,'https://www.tripadvisor.fr/Attractions-g187208-Activities-c63-Provence_Alpes_Cote_d_Azur.html'''''


urls=['https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11306-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11309-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11292-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11295-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12169-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12170-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12156-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft11312-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12159-Provence_Alpes_Cote_d_Azur.html', 'https://www.tripadvisor.fr/Attractions-g187208-Activities-zft12163-Provence_Alpes_Cote_d_Azur.html']
import time
import random
def getter(z):

    browser = webdriver.Chrome(options=chrome_options,executable_path="C://bin//chromedriver.exe")
    browser.get(z)
    print(z)
    indexy=urls.index(z)
    time.sleep(random.uniform(1,1.5))
    #browser.save_screenshot('test'+urls.index(z)+'.png')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(1,1.5))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(1,1.5))
    timestamp=str(int(time.time()))
    browser.save_screenshot('C://Users//f.bonnefoy//Desktop//Trippy//test'+timestamp+'.png')
    element=browser.find_element_by_css_selector("a.ui_button.nav.next.primary")
    content=browser.page_source
    sopa=soup(content,'html.parser')
    scrape=sopa.findAll('a',{'class':'_1QKQOve4'})
    time.sleep(random.uniform(0.5,1.5))
    with open('tripurl_attr.txt','a') as f:
        for a in scrape:
            print('https://www.tripadvisor.fr'+a['href'],file=f)
    element.click()
    while True:
        try:


            time.sleep(random.uniform(1,1.5))
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            timestamp=str(int(time.time()))
            browser.save_screenshot('C://Users//f.bonnefoy//Desktop//Trippy//test'+timestamp+'.png')
            content=browser.page_source
            sopa=soup(content,'html.parser')
            element=browser.find_element_by_css_selector("a.ui_button.nav.next.primary")
            scrape=sopa.findAll('a',{'class':'_1QKQOve4'})
            with open('tripurl_attr.txt','a') as f:
                for a in scrape:
                    print('https://www.tripadvisor.fr'+a['href'],file=f)
            element.click()
        except:
            break

for a in urls:
    getter(a)

'''
with ThreadPoolExecutor(max_workers=2) as executor:
    future_results = [executor.submit(getter, url) for url in urls]
    results=[]
    for future in as_completed(future_results):
        results.append(future.result())
'''
