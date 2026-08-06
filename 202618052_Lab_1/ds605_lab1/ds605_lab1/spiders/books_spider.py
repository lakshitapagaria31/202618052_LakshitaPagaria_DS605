import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        # Figure out our current catalog page, defaulting to page 1 when we first start
        current_page = response.meta.get('page', 1)

        # Grab all book links on the main page and jump into each book's individual page
        book_links = response.css('h3 a::attr(href)').getall()
        for link in book_links:
            yield response.follow(link, callback=self.parse_book)

        # Find the "Next" page button and keep moving forward until we hit page 6
        next_page = response.css('li.next a::attr(href)').get()
        if next_page and current_page < 6:
            yield response.follow(
                next_page, 
                callback=self.parse, 
                meta={'page': current_page + 1}
            )

    def parse_book(self, response):
        # Pull raw availability text and clean up all the weird spaces and newlines
        availability_raw = response.css('p.instock.availability::text').getall()
        clean_availability = "".join(availability_raw).strip()

        # Collect all required book information directly from the product page
        yield {
            'title': response.css('div.product_main h1::text').get(),
            'category': response.css('ul.breadcrumb li:nth-child(3) a::text').get(),
            'price': response.css('p.price_color::text').get(),
            'rating': response.css('p.star-rating::attr(class)').get(),
            'availability': clean_availability,
            'product_description': response.css('div#product_description + p::text').get(),
            'UPC': response.xpath('//th[text()="UPC"]/following-sibling::td/text()').get(),
            'number_of_reviews': response.xpath('//th[text()="Number of reviews"]/following-sibling::td/text()').get(),
            'product_url': response.url,
        }