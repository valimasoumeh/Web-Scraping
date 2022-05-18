import scrapy
from scrapy import Selector
from selenium import webdriver
from datetime import datetime

  

class Var3MessiSpider(scrapy.Spider):
    name = 'Var3MessiSpider'
    allowed_domains = ["varzesh3.com"]
    start_urls = ['https://www.varzesh3.com/player/1546/%d9%84%db%8c%d9%88%d9%86%d9%84-%d9%85%d8%b3%db%8c']
    
    def parse(self, response):
        driver = webdriver.Firefox()
        driver.get(self.start_urls[0])
        max_date = datetime.strptime('2018-01-01', '%Y-%m-%d')
        while True:
            next_url = driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div[2]/div[1]/button')
            try:
                # click the button to go to next page 
                next_url.click()
            except:
                break
            sel = driver.page_source
            selen = Selector(text=sel)
            break_points = selen.css('div.team-page--news-list-area')
            last_date = break_points.css('div.period-breakpoint')[-1].attrib['data-time']
            # last_date_object = datetime.strptime(last_date, '%Y-%m-%d')
            if last_date[0:4] == '2018':
                break

        driver.close()
        # date = response.css('div.period-breakpoint').attrib['data-time']
        for products in selen.css('div.tp-news-detail-wrapper'):
            link = products.css('a.title').attrib['href']
            yield response.follow(link, callback=self.parse_news)
            
    def parse_news(self, response):
            yield{
                'Title': response.css('h1.news-page--news-title::text').get(),
                'Sumary': response.css('p.news-page--news-lead.text-justify::text').get(),
                'Text': response.css('div.col-xs-12.news-page--news-text.text-justify p::text').getall(),
                'Date': response.css('span.numeric-value::text')[2].get(),
                'View': response.css('span.numeric-value::text')[3].get()
            }
