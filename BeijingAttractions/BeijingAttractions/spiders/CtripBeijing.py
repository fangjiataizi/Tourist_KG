import scrapy
from BeijingAttractions.items import BeijingAttractionsItem
import re
import json

class CtripBeijingSpider(scrapy.Spider):
    name = 'ctrip_beijing'
    allowed_domains = ['you.ctrip.com']
    start_urls = ['https://you.ctrip.com/sight/beijing1.html']

    def parse(self, response):
        # 解析首页
        for sight in response.css('div.list_mod2'):
            item = BeijingAttractionsItem()
            item['name'] = sight.css('dt a::attr(title)').get()
            item['hot_score'] = sight.css('.hot_score_number::text').get()
            review_text = sight.css('.recomment::text').get()
            review_count_match = re.search(r'(\d+)', review_text)
            item['review_count'] = int(review_count_match.group(1)) if review_count_match else 0
            # item['review_count'] = int(review_text.strip('()条点评')) if review_text else 0
            item['rating'] = sight.css('.score strong::text').get()
            address = sight.css('dd.ellipsis::text').get()
            item['address'] = re.sub(r'\s+', '', address) if address else None
            # 在您的parse方法中，对于每个字段，使用正则表达式去除多余的空白字符
            # item['address'] = re.sub(r'\s+', '', sight.css('dd.ellipsis::text').get())
            # item['comment'] = sight.css('p.bottomcomment::text').get()
            comment = sight.css('p.bottomcomment::text').get()
            item['comment'] = re.sub(r'\s+', '', comment) if comment else None
            # item['comment'] = re.sub(r'\s+', '', sight.css('p.bottomcomment::text').get())
            detail_url = sight.css('dt a::attr(href)').get()
            item['url'] = response.urljoin(detail_url)
            print(item)
            yield item
        # 分页
        next_page = response.css('.nextpage::attr(href)').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
