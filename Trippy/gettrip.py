import support as sp
import time
def getter(z):

    sp.open_session_firefox()
    sp.change(z)
    time.sleep(random.uniform(1,1.5))
    #browser.save_screenshot('test'+urls.index(z)+'.png')
    sp.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(0.5,1))
    sp.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(0.5,1))
    timestamp=str(int(time.time()))
    sp.browser.save_screenshot(timestamp+'.png')
    element=sp.browser.find_element_by_css_selector("a.ui_button.nav.next.primary")
    content=sp.browser.page_source
    sopa=sp.soup(content,'html.parser')
    scrape=sopa.findAll('a',{'class':'_1QKQOve4'})
    time.sleep(random.uniform(0.5,1))
    with open('tripurl_attr.txt','a') as f:
        for a in scrape:
            print('https://www.tripadvisor.fr'+a['href'],file=f)
    element.click()
    while True:
        try:
            time.sleep(random.uniform(0.5,1))
            sp.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            timestamp=str(int(time.time()))
            sp.browser.save_screenshot(timestamp+'.png')
            content=sp.browser.page_source
            sopa=sp.soup(content,'html.parser')
            element=sp.browser.find_element_by_css_selector("a.ui_button.nav.next.primary")
            scrape=sopa.findAll('a',{'class':'_1QKQOve4'})
            with open('tripurl_attr.txt','a') as f:
                for a in scrape:
                    print('https://www.tripadvisor.fr'+a['href'],file=f)
            element.click()
        except:
            break
