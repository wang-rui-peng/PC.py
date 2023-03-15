# 双色球
import requests
import csv # 内置模块
# 发送请求的url地址
url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice'

params = {
    'name': 'ssq',
    'issueCount': '',
    'issueStart': '',
    'issueEnd': '',
    'dayStart': '2017-10-24',
    'dayEnd': '2023-03-14',
    'pageNo': 'page'
}
headers = {
    'Referer': 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
response = requests.get(url=url, params=params, headers=headers)
for index in response:
    dit = {
        '期号': index['code'],
        '开奖日期': index['date'],
        '红球': index['red'],
        '蓝球': index['blue'],
        '一等奖中奖注数': index['prizegrades'][0]['typenum'],
        '一等奖中奖金额': index['prizegrades'][0]['typemoney'],
        '二等奖中奖注数': index['prizegrades'][1]['typenum'],
        '二等奖中奖金额': index['prizegrades'][1]['typemoney'],
        '三等奖中奖注数': index['prizegrades'][2]['typenum'],
        '三等奖中奖金额': index['prizegrades'][2]['typemoney'],
        '四等奖中奖注数': index['prizegrades'][3]['typenum'],
        '四等奖中奖金额': index['prizegrades'][3]['typemoney'],
        '五等奖中奖注数': index['prizegrades'][4]['typenum'],
        '五等奖中奖金额': index['prizegrades'][4]['typemoney'],
        '六等奖中奖注数': index['prizegrades'][5]['typenum'],
        '六等奖中奖金额': index['prizegrades'][5]['typemoney'],
        '一等奖中奖地区': index['content'],
        '奖池金额': index['poolmoney']
    }


f = open('双色球.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['期号',
                                '开奖日期',
                                '红球',
                                '蓝球',
                                '一等奖中奖注数',
                                '一等奖中奖金额',
                                '二等奖中奖注数',
                                '二等奖中奖金额',
                                '三等奖中奖注数',
                                '三等奖中奖金额',
                                '四等奖中奖注数',
                                '四等奖中奖金额',
                                '五等奖中奖注数',
                                '五等奖中奖金额',
                                '六等奖中奖注数',
                                '六等奖中奖金额',
                                '一等奖中奖地区',
                                '奖池金额'])

csv_writer.writeheader() # 写入表头
csv_writer.writerow(dit)
print(dit)
# 大乐透
