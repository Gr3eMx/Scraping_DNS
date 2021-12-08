import json
from selenium import webdriver

def get_number_page():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument(f"--proxy-server={'85.117.233.102:65233'}")
        options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        browser = webdriver.Chrome(options=options)
        browser.get("https://www.dns-shop.ru/catalog/17a9cccc16404e77/termointerfejsy/?order=6&q=%D1%82%D0%B5%D1%80%D0%BC%D0%BE%D0%BF%D0%B0%D1%81%D1%82%D0%B0&stock=0&p=0")
        get_last_count = browser.find_element_by_class_name("pagination-widget__page-link_last")
    finally:
        browser.close()
        browser.quit()
    count = int(get_last_count.get_attribute('href')[-2:])
    return count

elements2 = []
url2 = []
id1 = []
id2 = []
numbers = []

def scrapingDNS(count):
    for c in range(1, count):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument(f"--proxy-server={'85.117.233.102:65233'}")
            options.add_argument(
                f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
            options.add_argument("--disable-blink-features=AutomationControlled")
            browser = webdriver.Chrome(options=options)
            browser.get(f"https://www.dns-shop.ru/catalog/17a9cccc16404e77/termointerfejsy/?order=6&q=%D1%82%D0%B5%D1%80%D0%BC%D0%BE%D0%BF%D0%B0%D1%81%D1%82%D0%B0&stock=0&p={c}")
            elements = browser.find_elements_by_class_name('catalog-product__name')
            url_items = browser.find_elements_by_class_name('catalog-product__name')
            id_items = browser.find_elements_by_css_selector("div[data-id='product']")
            for l in range(1,count+1):
                numbers.append(l)
            for z in elements:
                elements2.append(z.text)
            for k in url_items:
                url2.append(k.get_attribute('href'))
            for k in id_items:
                id1.append(k.get_attribute('data-code'))
            for z in id_items:
                id2.append(z.get_attribute('data-product'))
            keys = ['name','number','url','id1','id2']

            zipped = zip(elements2, numbers, url2, id1,id2)
            dicts = [dict(zip(keys, values)) for values in zipped]
        finally:
            browser.close()
            browser.quit()

    with open('dicts.json', 'w', encoding='utf-8') as file:
        json.dump(dicts, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    get_number_page()
    scrapingDNS(get_number_page())
