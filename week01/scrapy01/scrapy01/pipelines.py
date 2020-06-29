# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class Scrapy01Pipeline:
    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):

        movie_title = item['movie_title']
        movie_type = item['movie_type']
        movie_time = item['movie_time']

        mytuple = [(movie_title, movie_time, movie_type)]
        movielist = pd.DataFrame(data=mytuple)

        # windows需要使用gbk字符集
        movielist.to_csv('./maoyan_movie2.csv', encoding='gbk', index=False, header=False, mode='a+')

        # movie_title = item['movie_title']
        # movie_type = item['movie_type']
        # movie_time = item['movie_time']
        # output = f'|{movie_title}|\t|{movie_type}|\t|{movie_time}|\n\n'
        # with open('./maoyan.txt', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        return item