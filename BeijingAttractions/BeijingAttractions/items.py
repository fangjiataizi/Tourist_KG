import scrapy

class BeijingAttractionsItem(scrapy.Item):
    name = scrapy.Field()           # 景点名称
    hot_score = scrapy.Field()      # 热度
    review_count = scrapy.Field()   # 评论数量
    rating = scrapy.Field()         # 评分
    address = scrapy.Field()        # 景点地址
    comment = scrapy.Field()        # 一条点评
    detail_url = scrapy.Field()     # 景点详情页链接
    opening_hours = scrapy.Field()  # 开放时间
    url= scrapy.Field()              # 景点链接
    # 根据需要您可能会添加更多的字段