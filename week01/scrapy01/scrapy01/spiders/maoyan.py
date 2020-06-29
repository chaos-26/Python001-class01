# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy01.items import Scrapy01Item


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
            yield scrapy.Request(
                self.start_urls[0],
               # url=start_urls,
                callback=self.parse,
               #  headers={
               #      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400',
               #      'Cookie': '__mta=248469816.1593078089508.1593340886507.1593340890715.11; uuid_n_v=v1; uuid=09CF0CA0B6C811EA842AD7B3BE0152F21C3E83A6752D4E8C87ED10E559B7E78C; mojo-uuid=10f95cca5789948a5aff508a83c95008; _lxsdk_cuid=172eada866a39-032c14eaff82ef-335e4e71-fa000-172eada866bc8; _lxsdk=09CF0CA0B6C811EA842AD7B3BE0152F21C3E83A6752D4E8C87ED10E559B7E78C; __mta=248469816.1593078089508.1593078089508.1593078089508.1; _csrf=9d2eb19ea4343f1b1015b61cae0b8f4ff2b7a4f23eadce6b05c70dd0de9f9bbc; mojo-session-id={"id":"ebc7d39620d797602b7309621196d8ca","time":1593340715421}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593090824,1593090900,1593090951,1593340715; mojo-trace-id=4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593340890; _lxsdk_s=172fa81e1cb-227-11d-bf9%7C%7C8'
               # }
            )
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    def parse(self, response):
        title_list = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        #print(title_list)
        for i in range(1,11):
            #print(title_list[i])
            item = Scrapy01Item()
            title = title_list[i].xpath('./a/text()').extract_first().strip()
            #print(title)
            link = title_list[i].xpath('./a/@href').extract_first().strip()
            mylink = 'https://maoyan.com' + link
            #print(mylink)
            yield scrapy.Request(url= mylink, meta={'item': item}, callback=self.parse2)
   #         print(scrapy.Request)

    def parse2(self, response):
        movie_type_list = []
        amovie = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        #print(amovie)
        for amovie_type in amovie.xpath('./ul/li/a/text()'):
            movie_type_list.append(amovie_type.extract().strip())
            #print(amovie_type.extract())
        movie_type_str = ','.join(movie_type_list)
        print(movie_type_str)
      #  print(title_list2.xpath('./a/text()'))
        #item = response.meta['item']
        #print(item)
        # item['content'] = content
        # yield item
    # 解析函数
    # def parse(self, response):
    #     # 打印网页的url
    #     #print(response.url)
    #     # 打印网页的内容
    #     print(response.text)
    #
    #     # soup = BeautifulSoup(response.text, 'html.parser')
    #     # title_list = soup.find_all('div', attrs={'class': 'hd'})
    #     movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[2]')
    #     for movie in movies:
    #     #     title = i.find('a').find('span',).text
    #     #     link = i.find('a').get('href')
    #         # 路径使用 / .  .. 不同的含义　
    #         title = movie.xpath('./a/text()')
    #         link = movie.xpath('./a/@href')
    #         print('-----------')
    #         print(title)
    #         print(link)
    #         # print('-----------')
    #         # print(title.extract())
    #         # print(link.extract())
    #         # print(title.extract_first())
    #         # print(link.extract_first())
    #         # print(title.extract_first().strip())
    #         # print(link.extract_first().strip())