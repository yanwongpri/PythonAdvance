# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

import requests
import bs4
import pandas as pd

SYMBOL_YEBAO = '000198'


def obtain_info_of_data(symbol):
    response = requests.get('http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=' + str(symbol))
    # return format: var apidata={...};
    # filter the tag
    content = str(response.text.encode('utf8')[13:-2])
    content_split = content.split(',')
    # obtain the info of data, curpage, pages, records
    curpage = content_split[-1].split(':')[-1]
    pages = content_split[-2].split(':')[-1]
    records = content_split[-3].split(':')[-1]
    return {'curpage': curpage, 'pages': pages, 'records': records}



def obtain_data(symbol, dict_data_info):
    cur_pages = int(dict_data_info['pages'])
    pages = dict_data_info['pages']
    records = dict_data_info['records']

    data_return = []

    url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&page=%s'

    for cp in range(int(pages), 0, -1):
        response = requests.get(url % (symbol, str(cp)))
        content = response.text.encode('utf8')[13:-2]
        data = content.split(',')[0][10:-1]
        data_soup = bs4.BeautifulSoup(data, 'lxml')
        line_of_data = len(data_soup.select('table > tbody > tr'))

        for i in range(line_of_data, 0, -1):
            row_of_data = []
            date = data_soup.select('table > tbody > tr:nth-of-type(%i) > td:nth-of-type(1)' % i)[0].text
            earning_per_10k = data_soup.select('table > tbody > tr:nth-of-type(%i) > td:nth-of-type(2)' % i)[0].text
            annualized_return = data_soup.select('table > tbody > tr:nth-of-type(%i) > td:nth-of-type(3)' % i)[0].text
            row_of_data.append(date)
            row_of_data.append(earning_per_10k)
            row_of_data.append(annualized_return)
            data_return.append(row_of_data)
        print 'Finished %i' % cp
        cur_pages -= 1
        if cur_pages == 1 and len(data_return) != int(records):
            print 'Data Missing..'
    return pd.DataFrame(data_return)

if __name__ == '__main__':
    data_info = obtain_info_of_data(SYMBOL_YEBAO)
    rs = obtain_data(SYMBOL_YEBAO, data_info)
    print rs