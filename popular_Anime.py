import scrapy


class animeSpyder(scrapy.Spider):
    name = 'anime'
    page_number = 2
    start_urls = [
        'https://mangakakalot.com/manga_list?type=topview&category=all&state=all&page=1']
    
    def parse(self, response):

        main = response.css("div.list-truyen-item-wrap")
        # all_div_quotes = response.css("div.quote")

        for ani in main:
            
            title = ani.css("a").attrib['title']
            views = ani.css("span.aye_icon::text").extract()
            description = ani.css("p::text").extract()

            
            yield {'title':title, 'views':views, 'description':description} 
        
        next_page = 'https://mangakakalot.com/manga_list?type=topview&category=all&state=all&page='+ str(animeSpyder.page_number) + '/'
        if animeSpyder.page_number  < 11:
            animeSpyder.page_number +=1
            yield response.follow(next_page, callback = self.parse)