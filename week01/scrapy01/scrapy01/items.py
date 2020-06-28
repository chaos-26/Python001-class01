# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    movie_title = scrapy.Field()
    movie_type = scrapy.Field()
    movie_time = scrapy.Field()
    movie_link = scrapy.Field()
