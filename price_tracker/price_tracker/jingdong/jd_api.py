# coding: utf-8
# 京东价格API
import requests
from bs4 import BeautifulSoup
import re

re_get_id = re.compile('.+/(?P<item_id>\d+).+')


def get_jd_id_price(url):
    '''
    JD API: https://p.3.cn/prices/mgets?&skuIds={id}
    :return: id, 京东当前价格
    '''
    id = re.match(re_get_id, url).group('item_id')
    res = requests.get(url='https://p.3.cn/prices/mgets?&skuIds=J_' + id, verify=False)
    res.encoding = 'utf-8'
    return id, res.json()[0].get('p')


def add_item(url):
    '''
    向jd_item中追加商品
    :param url: 商品url
    :return:   1 添加成功
               0 添加失败
    '''
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'lxml')
    res.encoding = 'utf-8'
    temp = soup.select('head > title')[0].text
    item_name = re.fullmatch('(【.+】)?(?P<item_name>[^【】]+)【.*', temp).group('item_name')
    # print(item_name)
    item_id = re.match(re_get_id, url).group('item_id')
    try:
        # jd_item 绝对路径
        # with open('F:\\project\\price_tracker\\price_tracker\\jingdong\\jd_item', 'a', encoding='utf-8') as jd_item:
        with open('/home/price_tracker/price_tracker/jingdong/jd_item', 'a', encoding='utf-8') as jd_item:
            add = item_id + ': ' + item_name + '\n'
            jd_item.write(add)
            return True
    except Exception as error:
        print(error)
        return False


# add_item(url='https://item.jd.hk/1975463255.html')
# add_item(url='https://item.jd.com/1115705656.html')
