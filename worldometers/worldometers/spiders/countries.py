import scrapy
import logging
class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # Assuming you want all <a> within <td> throughout the document:
        countries = response.xpath("//td/a") 

        for country in countries:
            name = country.xpath("./text()").get()  # Get text directly within <a>
            link = country.xpath("./@href").get()  # Get href attribute of <a>
            
            # Bai1:
            # yield {
            #     'country_name': name,
            #     'country_link': link
            # }
            
            # Bai2:
            # yield response.follow(url=link)  
            # Bai3:
            # yield response.follow(url=link, callback=self.parse_country)
            # Bai4:
            yield response.follow(url=link, callback=self.parse_country, meta = {'country_name': name})
            
    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath("./td[1]/text()").get()
            population = row.xpath("./td[2]/strong/text()").get()
            yield {
                'name': name,
                'year': year,
                'population': population
            }
#scrapy parse --spider=countries -c parse_country --meta='{\"country_name\":\"India\"}' https://www.worldometers.info/world-population/india-population/