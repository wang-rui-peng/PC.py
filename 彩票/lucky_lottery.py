# 双色球
import requests
import csv  # 内置模块
import pandas as pd
import os

# file=f'D:\python\PC\彩票\'


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'HMF_CI=e1595b50b4a6b2983421ac2835d9d471bba8072c7dd9bcac1a3c1b227b0c5138aa5a3e3a957a6e694c58e7258230d9e135a2062c698dba77ea959de8bc49b7335c; 21_vq=27',
    'Host': 'www.cwl.gov.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://www.cwl.gov.cn/ygkj/wqkjgg/ssq/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}


# 抓取数据并记入文件
def crawl_write_to_csv():
    if os.path.exists('双色球.csv'):
        os.remove('双色球.csv')
        print('双色球.csv文件已删除!')
    else:
        print('双色球.csv文件不存在!')

    # 生成CSV文件
    f = open('双色球.csv', mode='a', newline='', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(
        ['期数', '日期', '红球', '蓝球', '销售额', '奖池金额', '一等奖人数', '一等奖金额', '二等奖人数', '二等奖金额',
         '三等奖人数', '三等奖金额', '四等奖人数', '四等奖金额', '五等奖人数', '五等奖金额', '六等奖人数', '六等奖金额',
         '中奖情况'])

    for page in range(1, 54):  # 获取每一页记录
        print(f'正在抓取第{page}页>>>>>>')
        # 发送请求的url地址
        url = f'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=&dayEnd=&pageNo={page}&pageSize=30&week=&systemType=PC'

        response = requests.get(url=url, headers=headers)
        json_data = response.json()
        # result-->0-->red
        result = json_data['result']
        for res in result:
            code = res['code']
            data = res['date']
            reds = res['red']
            blues = res['blue']
            sales = res['sales']
            poolmoney = res['poolmoney']
            prizegrades = res['prizegrades']
            one_prize, one_price, two_prize, two_price, three_prize, three_price, four_prize, four_price, five_prize, five_price, six_prize, six_price = '', '', '', '', '', '', '', '', '', '', '', ''
            for prizegrad in prizegrades:
                if prizegrad['type'] == 1:
                    one_prize = prizegrad['typenum']
                    one_price = prizegrad['typemoney']
                elif prizegrad['type'] == 2:
                    two_prize = prizegrad['typenum']
                    two_price = prizegrad['typemoney']
                elif prizegrad['type'] == 3:
                    three_prize = prizegrad['typenum']
                    three_price = prizegrad['typemoney']
                elif prizegrad['type'] == 4:
                    four_prize = prizegrad['typenum']
                    four_price = prizegrad['typemoney']
                elif prizegrad['type'] == 5:
                    five_prize = prizegrad['typenum']
                    five_price = prizegrad['typemoney']
                elif prizegrad['type'] == 6:
                    six_prize = prizegrad['typenum']
                    six_price = prizegrad['typemoney']
            content = res['content']
            # print(data, reds, blues, code, sales, poolmoney, one_prize, one_price, two_prize, two_price,
            #       three_prize, three_price, four_prize, four_price, five_prize, five_price, six_prize, six_price,
            #       content)
            # 保存为表格 期数，开奖日期，红球，篮球奖池金额，一等奖中奖人数，一等奖中奖金额，二等奖中奖人数，二等奖中奖金额，三等奖中奖人数，三等奖中奖金额，四等奖中奖人数，四等奖中奖金额，五等奖中奖人数，五等奖中奖金额，六等奖中奖人数，六等奖中奖金额，中奖情况，
            csv_writer.writerow(
                [code, data, reds, blues, sales, poolmoney, one_prize, one_price, two_prize, two_price,
                 three_prize, three_price, four_prize, four_price, five_prize, five_price, six_prize, six_price,
                 content])


# 把csv文件转换成excel文件
def csv_change_excel():
    # 读取 csv 文件
    df = pd.read_csv('双色球.csv', encoding='utf-8')

    if os.path.exists('彩票.xlsx'):
        print('彩票.xlsx文件已经存在!')
    else:
        pf = pd.DataFrame()
        pf.to_excel('彩票.xlsx', sheet_name='双色球', index=False)
        print('彩票.xlsx文件已经创建成功!')
    # 将数据写入 excel 文件
    with pd.ExcelWriter('彩票.xlsx', mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        # if writer.book['Sheet1'] in writer.book:
        #     writer.book.remove(writer.book['Sheet1'])      #删除指定sheet页
        df.to_excel(writer, sheet_name='双色球', index=False)
        # 调整列宽
        ws = writer.book.active
        for i, col in enumerate(ws.columns):
            max_length = 0
            column = col[0].column_letter  # 获取列字母序号
            for cell in col:
                try:
                    # 获取单元格中最长的文本长度
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = max_length + 2  # 适配宽度多留较宽空隙
            ws.column_dimensions[column].width = adjusted_width

        # 保存并关闭Excel文件
        writer.save()
    print('文件已转换完成,请打开察看！')


if __name__ == '__main__':
    crawl_write_to_csv()
    csv_change_excel()
