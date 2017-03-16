# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

import datetime
import requests
import bs4


'''
Symbol
    000198 -> YuEBao
    000961 -> TianHongHuShen300
'''

# Obatin and paser the parse from http://fund.eastmoney.com
def obtain_paser_fund_eastmoney(symbol):
    now = datetime.datetime.utcnow()

    response = requests.get(
        "http://fund.eastmoney.com/" + str(symbol) + ".html?spm=aladin"
    )
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    try:
        # Like YuEBao earning per 10K, css selector like below
        # If symbol not money fund like YuEBao, using this selector will be throw an IndexError
        price = soup.select('#body > div.whiteBG > div:nth-of-type(9) > div > div > div.fundDetail-main > div.fundInfoItem > div.dataOfFund.dataOfFund_hb > dl.dataItem01 > dd > span')[0].text
    except IndexError:
        # Index fund like TianHongHuShen300, css selector like below
        price = soup.select('#gz_gsz')[0].text
    return float(price)


if __name__ == '__main__':
    yebao_price = obtain_paser_fund_eastmoney('000198')
    print 'YuEBao -> %f' % (float(yebao_price) / 10000.0)
    thhs300 = obtain_paser_fund_eastmoney('000961')
    print 'TianHongHuShen300 -> %f' % float(thhs300)