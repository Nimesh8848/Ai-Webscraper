from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection


AUTH = 'brd-customer-hl_05fddee9-zone-ai_scraper:ikx8edz1x7os'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(website):
    print("Launching Browser...")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
       
        driver.get(website)
        print('Waiting Capta to Resolve...')
        solve_res=driver.execute(
            'send_command',
            {
                'cmd': 'solveRecaptchaV2',
                'params':{'detectTimeout': 10000}
            },
        )
        print('Captcha Solved Status:',solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        print(html)
   




