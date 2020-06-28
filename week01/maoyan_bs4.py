# 使用BeautifulSoup解析网页

import requests
import re
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd
# bs4是第三方库需要使用pip命令安装

#request参数
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
mycookie='__mta=248469816.1593078089508.1593340886507.1593340890715.11; uuid_n_v=v1; uuid=09CF0CA0B6C811EA842AD7B3BE0152F21C3E83A6752D4E8C87ED10E559B7E78C; mojo-uuid=10f95cca5789948a5aff508a83c95008; _lxsdk_cuid=172eada866a39-032c14eaff82ef-335e4e71-fa000-172eada866bc8; _lxsdk=09CF0CA0B6C811EA842AD7B3BE0152F21C3E83A6752D4E8C87ED10E559B7E78C; __mta=248469816.1593078089508.1593078089508.1593078089508.1; _csrf=9d2eb19ea4343f1b1015b61cae0b8f4ff2b7a4f23eadce6b05c70dd0de9f9bbc; mojo-session-id={"id":"ebc7d39620d797602b7309621196d8ca","time":1593340715421}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593090824,1593090900,1593090951,1593340715; mojo-trace-id=4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593340890; _lxsdk_s=172fa81e1cb-227-11d-bf9%7C%7C8'
header = {'user-agent':user_agent,'cookie':mycookie}
myurl = 'https://maoyan.com/board/4'

#初始化cvs表
mytuple = [('电影名称','上映时间','电影类型')]
movielist = pd.DataFrame(data=mytuple)
movielist.to_csv('./maoyan_movie.csv', encoding='gbk', index=False, header=False,mode='w')

#获取响应
response = requests.get(myurl,headers=header)
bs_info = bs(response.text, 'html.parser')

# 获取电影名称、电影类型、电影上映时间
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}):
    #print(tags)
    # 获取电影名字
    movie_name=tags.find('a',).text
    # 获取上映日期,只取第一个上映时间，去除上映地点信息
    atime=tags.find(attrs={'class': 'releasetime'}).text
    movie_time=re.split(r'[:：（(]',atime)[1].strip()


    movieurl='https://maoyan.com' + (tags.find('a',).get('href'))
    movieresponse = requests.get(movieurl, headers=header)
    movie_bs_info = bs(movieresponse.text, 'html.parser')
    #获取详情页链接
    movie_type = []
    for movietags in movie_bs_info.find_all('div', attrs={'class': 'movie-brief-container'}):
        for amovietags in movietags.find_all('a', ):
            #print(amovietags)
            movie_type.append((amovietags.text).strip())
        sleep(2)
    movie_type_str = ','.join(movie_type)
    #数组转成字符串
    #print(movie_type_str)
    # #将结果写入CSV文件
    mytuple=[(movie_name,movie_time,movie_type_str)]
    movielist = pd.DataFrame(data = mytuple)

    # windows需要使用gbk字符集
    movielist.to_csv('./maoyan_movie.csv', encoding='gbk', index=False, header=False,mode='a+')

