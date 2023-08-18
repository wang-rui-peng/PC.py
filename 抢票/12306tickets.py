"""
[课程内容]: Python实现12306购票程序

[授课老师]: 青灯教育-自游  [上课时间]: 20:05  可以点歌 可以问问题

[环境使用]:
    Python 3.8
    Pycharm

[模块使用]:
    requests
    prettytable
    selenium --> pip install selenium==3.141.0 版本
    谷歌浏览器
    谷歌驱动

素材: 找木子老师微信领取
    city.json 城市文件
    驱动安装教程

案例分为两部分:
    1. 查票 --> 爬虫 采集车次信息 √
    2. 购票

爬虫采集车次信息 <爬虫基本思路>

1. 明确需求:
    - 明确采集网站以及数据内容
        网址: https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E9%95%BF%E6%B2%99,CSQ&ts=%E4%B8%8A%E6%B5%B7,SHH&date=2023-07-10&flag=N,N,Y
        数据: 车次信息
    - 通过开发者工具进行抓包分析
        车次信息: https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2023-07-10&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=SHH&purpose_codes=ADULT


1. 发送请求, 模拟浏览器对于url地址发送请求
2. 获取数据, 获取服务器返回响应数据
3. 解析数据, 提取车次信息

一. 查票: 模拟浏览器去请求链接得到数据
二. 购票: 模拟人的行为去操作浏览器, 进行购买
    selenium --> 浏览器+浏览器驱动

本节课使用:
    谷歌浏览器 谷歌驱动
1. 打开浏览器
2. 访问网站
3. 输入账号密码登陆
4. 点击车票预定
5. 输入出发 目的 时间 点击查询
6. 点击具体车次预定车票
7. 选择乘车人 / 选择座位 / 提交订单
8. 确定购买

就业工作: 学会80%左右知识点
    爬虫工程师 / 开发工程师 / 数据分析师 / 算法工程师
    薪资待遇: 8000-15000 左右


接单 外包:
    最短2个月左右, 学完爬虫之后, 可以就接单
    外包价格: 200-5000不等
    人均月收入: 1000-3000左右

接单可以积累开发经验, 开发经验 --> 帮助你就业工作

学习路线图 --> 清风老师客服微信: pythonmiss



"""
# 导入数据请求模块
import requests
# 导入漂亮制表
import prettytable as pt
# 导入json模块
import json
# 导入selenium
from selenium import webdriver
# 导入账号密码
from password import Password
import account
from selenium.webdriver.common.keys import Keys
import time

def Buy(num, from_city, to_city, date):
    # 1. 打开浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 2. 访问网站
    driver.get('https://kyfw.12306.cn/otn/resources/login.html')
    # 3. 输入账号密码 --> css选择器和xpath
    driver.find_element_by_css_selector('#J-userName').send_keys(account)
    driver.find_element_by_css_selector('#J-password').send_keys(Password)
    driver.find_element_by_css_selector('#J-login').click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('#link_for_ticket').click()
    driver.implicitly_wait(10)

    driver.find_element_by_css_selector('#fromStationText').click()
    driver.find_element_by_css_selector('#fromStationText').clear()
    driver.find_element_by_css_selector('#fromStationText').send_keys(from_city)
    driver.find_element_by_css_selector('#fromStationText').send_keys(Keys.ENTER)

    driver.find_element_by_css_selector('#toStationText').click()
    driver.find_element_by_css_selector('#toStationText').clear()
    driver.find_element_by_css_selector('#toStationText').send_keys(to_city)
    driver.find_element_by_css_selector('#toStationText').send_keys(Keys.ENTER)

    driver.find_element_by_css_selector('#train_date').click()
    driver.find_element_by_css_selector('#train_date').clear()
    driver.find_element_by_css_selector('#train_date').send_keys(date)
    driver.find_element_by_css_selector('#query_ticket').click()
    driver.find_element_by_css_selector(f'#queryLeftTable tr:nth-child({int(num) *2 -1}) .btn72').click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('#normalPassenger_1').click()
    driver.find_element_by_css_selector('#submitOrder_id').click()
    time.sleep(3)
    driver.find_element_by_css_selector('#qr_submit_id').click()


# 读取json文件
f = open('city.json', encoding='utf-8')
# 读取内容
txt = f.read()
# 转成字典
json_data = json.loads(txt)
# 输入出发 目的 时间
from_city = input('请输入你要出发的城市: ')
to_city = input('请输入你要到达的城市: ')
date = '2023-07-10'
try:
    """
    1. 发送请求, 模拟浏览器对于url地址发送请求
        固定查票: 长沙->上海 2023-07-10

    根据用户个人需求, 用户自己输入出发地, 目的地, 时间
    """
    # 模拟浏览器 headers请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    # 请求链接
    url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2023-07-10&leftTicketDTO.from_station={json_data[from_city]}&leftTicketDTO.to_station={json_data[to_city]}&purpose_codes=ADULT'
    # 发送请求 <Response [200]> 响应对象 表示请求成功
    response = requests.get(url, headers=headers)
    """
    2. 获取数据, 获取服务器返回响应数据
        response.json() 获取响应json数据
            <字典数据类型>
    3. 解析数据, 提取车次信息
        字典取值 键值对取值: 根据冒号左边内容<键>, 提取冒号右边的内容<值>
    """
    # 实例化对象
    tb = pt.PrettyTable()
    # 设置表头
    tb.field_names = [
        '序号',
        '车次',
        '出发时间',
        '到达时间',
        '耗时',
        '特等座',
        '一等',
        '二等',
        '软卧',
        '硬卧',
        '硬座',
        '无座',
    ]
    page = 1
    # for循环遍历, 提取列表里面元素
    for i in response.json()['data']['result']:
        # 字符串分割, 把数据进行分割取值
        index = i.split('|')

        # 根据列表索引位置取值
        num = index[3]  # 车次
        start_time = index[8]  # 出发时间
        end_time = index[9]  # 到达时间
        use_time = index[10]  # 耗时
        topGrade = index[32]  # 特等座
        if topGrade:
            topGrade = topGrade
        else:
            topGrade = index[25]
        first_class = index[31]  # 一等
        second_class = index[30]  # 二等
        hard_sleeper = index[28]  # 硬卧
        hard_seat = index[29]  # 硬座
        no_seat = index[26]  # 无座
        soft_sleeper = index[23]  # 软卧
        # dit = {
        #     '车次': num,
        #     '出发时间': start_time,
        #     '到达时间': end_time,
        #     '耗时': use_time,
        #     '特等座': topGrade,
        #     '一等': first_class,
        #     '二等': second_class,
        #     '软卧': soft_sleeper,
        #     '硬卧': hard_sleeper,
        #     '硬座': hard_seat,
        #     '无座': no_seat,
        # }
        tb.add_row([
            page,
            num,
            start_time,
            end_time,
            use_time,
            topGrade,
            first_class,
            second_class,
            soft_sleeper,
            hard_sleeper,
            hard_seat,
            no_seat,
        ])
        page += 1
    print(tb)
    car_num = input('请输入你要购买车次序号: ')
    Buy(car_num, from_city, to_city, date)



except Exception as e:
    print(e, '可能你输入的内容有误')