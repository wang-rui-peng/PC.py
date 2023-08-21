# 大乐透
import os
import requests
import csv  # 内置模块
import pandas as pd

# file=f'D:\python\PC\彩票\'


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Origin': 'https://static.sporttery.cn',
    'Referer': 'https://static.sporttery.cn/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}


# 抓取数据并记入文件
def crawl_write_to_csv():
    if os.path.exists('大乐透.csv'):
        os.remove('大乐透.csv')
        print('大乐透.csv文件已删除!')
    else:
        print('大乐透.csv文件不存在!')

    # 生成CSV文件
    f = open('大乐透.csv', mode='a', newline='', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(
        ['期号', '时间', '开奖号码', '奖池奖金', '销售额', '一等奖人数', '一等奖金额', '二等奖人数', '二等奖金额',
         '三等奖人数', '三等奖金额', '四等奖人数', '四等奖金额', '五等奖人数', '五等奖金额', '六等奖人数', '六等奖金额',
         '七等奖人数', '七等奖金额', '八等奖人数', '八等奖金额', '九等奖人数', '九等奖金额'])

    for page in range(1, 82):  # 获取每一页记录
        print(f'正在抓取第{page}页>>>>>>')
        # 发送请求的url地址
        url = f'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo={page}'

        response = requests.get(url=url, headers=headers)
        json_data = response.json()
        # value-->lotteryDrawResult-->lotteryDrawResult
        data = json_data['value']['list']
        for res in data:
            numbers = res['lotteryDrawNum']  # 销售期号
            times = res['lotteryDrawTime']  # 销售时间
            results = res['lotteryDrawResult']  # 开奖号码
            afterdraws = res['poolBalanceAfterdraw']  # 奖池奖金
            amounts = res['totalSaleAmount']  # 销售额
            # csv_writer.writerow([numbers, times, results, afterdraws, amounts])
            lists = res['prizeLevelList']
            one_prize, one_price, two_prize, two_price, three_prize, three_price, four_prize, four_price, five_prize, five_price, six_prize, six_price, seven_prize, seven_price, eight_prize, eight_price, nine_prize, nine_price = '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
            for prizeLevelList in lists:
                if prizeLevelList['prizeLevel'] == "一等奖":
                    one_prize = prizeLevelList['stakeCount']
                    one_price = prizeLevelList['totalPrizeamount']
                elif prizeLevelList['prizeLevel'] == "二等奖":
                    two_prize = prizeLevelList['stakeCount']
                    two_price = prizeLevelList['totalPrizeamount']
                elif prizeLevelList['prizeLevel'] == "三等奖":
                    three_prize = prizeLevelList['stakeCount']
                    three_price = prizeLevelList['totalPrizeamount']
                elif prizeLevelList['prizeLevel'] == "四等奖":
                    four_prize = prizeLevelList['stakeCount']
                    four_price = prizeLevelList['totalPrizeamount']
                elif prizeLevelList['prizeLevel'] == "五等奖":
                    five_prize = prizeLevelList['stakeCount']
                    five_price = prizeLevelList['totalPrizeamount']
                elif prizeLevelList['prizeLevel'] == "六等奖":
                    six_prize = prizeLevelList['stakeCount']
                    six_price = prizeLevelList['totalPrizeamount']
                elif prizeLevelList['prizeLevel'] == "七等奖":
                    seven_prize = prizeLevelList['stakeCount']
                    seven_price = prizeLevelList['totalPrizeamount']
                elif prizeLevelList['prizeLevel'] == "八等奖":
                    eight_prize = prizeLevelList['stakeCount']
                    eight_price = prizeLevelList['totalPrizeamount']
                elif prizeLevelList['prizeLevel'] == "九等奖":
                    nine_prize = prizeLevelList['stakeCount']
                    nine_price = prizeLevelList['totalPrizeamount']
            # print(numbers, times, results, afterdraws, amounts, one_prize, one_price, two_prize, two_price, three_prize,
            #       three_price, four_prize, four_price,
            #       five_prize, five_price, six_prize, six_price, seven_prize, seven_price, eight_prize, eight_price,
            #       nine_prize, nine_price)
            csv_writer.writerow(
                [numbers, times, results, afterdraws, amounts, one_prize, one_price, two_prize, two_price, three_prize,
                 three_price, four_prize, four_price,
                 five_prize, five_price, six_prize, six_price, seven_prize, seven_price, eight_prize, eight_price,
                 nine_prize, nine_price])


# 把csv文件转换成excel文件
def csv_change_excel():
    # 读取 csv 文件
    df = pd.read_csv('大乐透.csv', encoding='utf-8', error_bad_lines=False)

    if os.path.exists('彩票.xlsx'):
        print('彩票.xlsx文件已经存在!')
    else:
        pf = pd.DataFrame()
        pf.to_excel('彩票.xlsx', sheet_name='大乐透', index=False)
        print('彩票.xlsx文件已经创建成功!')
    # 将数据写入 excel 文件
    with pd.ExcelWriter('彩票.xlsx', mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='大乐透', index=False)

        # 调整列宽
        ws = writer.sheets['大乐透']
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
        '''
        #workbook = writer.book
        worksheet = writer.sheets['大乐透']
        # 遍历每一列并设置width ==该列的最大长度。填充长度也增加了2。
        for i, col in enumerate(df.columns):
            # 求列I的长度
            column_len = df[col].astype(str).str.len().max()
            # 如果列标题较大，则设置长度
            # 大于最大列值长度
            column_len = max(column_len, len(col)) + 2
            # 设置列的长度
            worksheet.set_column(i, i, column_len)
        writer.save()
        '''

    print('文件已转换完成,请打开察看！')


if __name__ == '__main__':
    crawl_write_to_csv()
    csv_change_excel()
