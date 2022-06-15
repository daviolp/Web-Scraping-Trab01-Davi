import scrapy


class WebScrapTesteSpider(scrapy.Spider):
    name = 'web_scrap_teste'
    allowed_domains = ['“quotes.toscrape.com']
    start_urls = ['http://“quotes.toscrape.com/']

    def parse(self, response):
        # XPath expression of all the Quote elements.
        # All quotes belong to CSS attribute class having value 'quote'
        quotes = response.xpath('//*[@class="quote"]')
        # Loop through the quotes object, to get required elements data.
        for quote in quotes:
            # XPath expression to fetch 'title' of the Quote
            # Title belong to CSS attribute class having value 'text'
            title = quote.xpath('.//*[@class="text"]/text()').extract_first()
            # XPath expression to fetch 'author name' of the Quote
            # Author name belong to CSS attribute itemprop having value 'author'
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            # XPath expression to fetch 'tags' of the Quote
            # Tags belong to CSS attribute itemprop having value 'keywords'
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
            # Return the output
            yield {'Text': title,
                   'Author': author,
                   'Tags': tags}
