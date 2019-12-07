import scrapy
import json

class quoteSpider(scrapy.Spider):
    name = 'quotes_scroll'
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'  
    start_urls = [api_url.format(1)
        ]
    
    def parse(self, response):
      
      data = json.loads(response.text)
      for quote in data['quotes']:
          yield {
              'author_name':quote['author']['name'],
              'tags':quote['tags'],
              'text':quote['text'],
              
          }
          if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(url = self.api_url.format(next_page), callback = self.parse)
