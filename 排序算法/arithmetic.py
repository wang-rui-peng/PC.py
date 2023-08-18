import time
import math

ls = [70, 15, 52, 55, 82, 3, 40, 17, 90, 1, 100, 23]


# 1 冒泡算法
def bubble_sort():
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    print("冒泡结果为：", ls)
    return ls


# 2 选择排序
def selection_sort():
    for i in range(len(ls) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            ls[i], ls[minIndex] = ls[minIndex], ls[i]
    print("选择结果为：", ls)
    return ls


# 3 插入排序
def insertion_sort():
    for i in range(len(ls)):
        preIndex = i - 1
        current = ls[i]
        while preIndex >= 0 and ls[preIndex] > current:
            ls[preIndex + 1] = ls[preIndex]
            preIndex -= 1
        ls[preIndex + 1] = current
    print("插入结果为：", ls)
    return ls


# 4 希尔排序
def shell_sort():
    gap = 1
    while gap < len(ls) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(ls)):
            temp = ls[i]
            j = i - gap
            while j >= 0 and ls[j] > temp:
                ls[j + gap] = ls[j]
                j -= gap
            ls[j + gap] = temp
        gap = math.floor(gap / 3)
    print("希尔结果为：", ls)
    return ls


# 5-1归并排序
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# noinspection PyShadowingNames
def merge_sort_1(ls):
    if len(ls) < 2:
        return ls
    #    num = math.floor(len(ls) / 2)
    num = int(len(ls) / 2)
    left, right = ls[0:num], ls[num:]
    resul = merge(merge_sort_1(left), merge_sort_1(right))
    return resul


# 5-2归并排序
# noinspection PyShadowingNames
def merge_sort_2(ls):
    length = len(ls)
    # 递归终止退出条件
    if length <= 1:
        return ls
    # 拆分
    mid = length // 2
    left_l = merge_sort_2(ls[:mid])  # 对左侧的列表进行排序
    right_l = merge_sort_2(ls[mid:])  # 对右侧的列表进行排序
    # merge 合并操作
    # 初始化两个指针p, q 初始位置为起始位置，初始化一个临时数组temp_list
    p, q, temp_list = 0, 0, list()
    len_left, len_right = len(left_l), len(right_l)  # 计算当前被合并的列表的长度
    while len_left > p and len_right > q:
        if left_l[p] <= right_l[q]:
            temp_list.append(left_l[p])
            p += 1
        else:
            temp_list.append(right_l[q])
            q += 1
    # 如果left 和 right 的长度不相等，把长的部分直接追加到列表中
    temp_list += left_l[p:]
    temp_list += right_l[q:]
    return temp_list


# 6.100以内的质数
def prime_number():
    a = []
    for num in range(2, 100):
        for n in range(2, num):
            if num % n == 0:
                break
        else:
            a.append(num)
    print('100以内的质数为：', a)


# 7.找出一段英文句子的最长的一个单词
import re


def selection_word():
    word = 'the stirng Has many line In THE fIle jb51 net'
    s2 = []
    max_word = 1
    word_list = re.split(r'\s+', word)
    # print(word_list)

    for words in word_list:
        if len(words) > max_word:
            s2 = [words]
            max_word = len(words)
    print('最长的一个单词为：', s2)


# 8.1-9的平方和
print('1-9的平方和为：', sum(i ** 2 for i in range(0, 10)))


# 9-1.99乘法表for-for语句
def multiplication_table_for():
    for i in range(0, 10):
        for j in range(1, i + 1):
            print('{}*{}={}'.format(j, i, j * i), end=' ')
        print('')


# 9-2 99乘法表while-while语句
def multiplication_table_while():
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            print(f'{j}*{i}={i * j}', end=' ')
            j += 1
        print('')
        i += 1


# 9-3.99乘法表列表推导式
def comprehensions():
    print('99乘法表为：',
          '\n'.join([' '.join(['%2s * %s = %2s' % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))


# 10-1.求已知时间的时间差
import datetime


def distences_time():
    start_time = '2022-09-07 19:30:00'
    end_time = '2022-09-07 19:37:00'
    start_time_str = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time_str = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    sec = (end_time_str - start_time_str).seconds
    print('两个时间点的时间差为：', sec)


# 10-2.求时间差
def time_times():
    # a = datetime.datetime.fromtimestamp(time.time())
    # start_time = datetime.datetime.now()
    # time.sleep(3)
    # end_time = datetime.datetime.now()
    # distance_time = end_time - start_time
    # print( a, start_time, end_time, distance_time)
    # return distance_time

    # a = time.time()  # 时间戳
    # b = time.localtime(a)
    # time.sleep(3)
    # c = time.time()
    # d = c - a
    # e = time.strftime('%Y-%m-%d %H:%M:%S')
    # print(a, c, d, e)

    # a = datetime.datetime.now()
    # time.sleep(3)
    # b = datetime.datetime.now()
    # c = ((b - a).seconds)
    # d = datetime.datetime.strftime(a, '%Y-%m-%d %H:%M:%S')
    # e = datetime.datetime.strftime(b, '%Y-%m-%d %H:%M:%S')
    # noinspection PyShadowingNames
    a = time.time()
    time.sleep(3)
    b = time.time()
    c = b - a
    d = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a))
    e = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(b))
    print('各个时间点为：', a, '\n', b, '\n', c, '\n', d, '\n', e)


# 11.列表逆序
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def stra():
    print('列表逆序结果为：', a[::-1])
    a.reverse()
    print('列表逆序结果为：', a)
    print('列表逆序结果为：', list(reversed(a)))


# 12.Matrix transposed（矩阵转置）
# 嵌套列表推导式（解析式）
def matrix_transposed():
    # 步骤1：设置一个嵌套列表 4*4
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12], ]
    # 步骤2：使用嵌套列表推导式（嵌套列表解析式）实现行列转换
    T = [[row[i] for row in matrix] for i in range(4)]
    # 步骤3：输出
    print('转置后的矩阵为：{0}'.format(T))


# 13.Fibonacci sequence（斐波那契数列）
# 13-1.使用while循环实现对位换值方式
def fibonacci_while_01():
    # 步骤1：接受控制台终端用户输入的数列个数
    items = int(input('请输入Fibonacci数列的个数：>'))
    # 步骤2：设置第0项和第1项的初始值
    n1 = 0
    n2 = 1
    count = 2
    # 步骤3：判断用户输入的的值是否合法
    if items <= 0:
        print('提示：请输入正整数\a')
        pass
    elif items == 1:
        # 若用户输入1，则只需显示n1的值即可
        print('Fibonacci数列：', n2)
        pass
    else:
        print('Fibonacci数列：', n2, end=', ')
        # 使用while循环
        while count <= items:
            # 计算新的数值（即前两项之合）
            res = n1 + n2
            # 输出新的数值
            print(res, end=', ')
            # 将前两项重新复制
            n1 = n2  # n2赋值给n1
            n2 = res  # 将res赋值给n2
            # 计数器自增1
            count += 1
            pass
        pass


# 13-2.While循环的实现
def fibonacci_while_02():
    # 步骤1：接受控制台终端用户输入的数列个数
    items = int(input('\n请输入Fibonacci数列的个数：>'))
    # 步骤2：设置第0项和第1项的初始值
    n1, n2 = 0, 1
    count = 1
    print('Fibonacci数列：')
    # 步骤3：使用while循环实现斐波那契数列
    while True:
        # 输出第2项的值
        print(n2, end=', ')
        count += 1  # 计数器自增1
        # 前两项更新值
        n1, n2 = n2, n1 + n2
        if count > 10: break
        pass
    pass


# 13-3.for循环实现的方法
def fibonacci_for():
    # 步骤1：接受控制台终端用户输入的数列个数
    items = int(input('\n请输入Fibonacci数列的个数：>'))
    # 步骤2：创建第0项和第1项列表
    fibs = [0, 1]
    # 步骤3：使用for循环实现斐波那契数列
    for i in range(items - 1):
        fibs.append(fibs[-2] + fibs[-1])
        pass
    # 步骤4：输出
    print('Fibonacci数列：', fibs[1:])
    pass


# 14.Armstrong number（阿姆斯特朗数）
# 使用Python3实现数值用户指定范围的阿姆斯特朗数
def armstrong():
    # 步骤1：接受用户输入的最小值和最大值范围
    minScope = int(input('最小值：>'))
    maxScope = int(input('最大值：>'))
    print('阿姆斯特朗数：')
    # 步骤2：for循环遍历取值范围并判断是否为阿姆斯特朗数
    for num in range(minScope, maxScope + 1):
        # 初始化累加变量
        total = 0
        # 获取当前数字的位数充当幂指数
        n = len(str(num))
        # 将num待判断数字备份
        temp = num
        # 使用while循环获取数字的各个位数幂次方累加和
        while temp > 0:
            digit = temp % 10  # 获取每个位数的值（个-> 十 -> 百 -> 千）
            total += digit ** n  # 计算当前位数的n次幂并进行累加
            temp //= 10  # 减少一位
            pass
        # 判断是否符合阿姆斯特朗数的规则
        if total == num:
            print(num, end=', ')
            pass
        pass


# 15.Factorial（阶乘）
# 使用Python3实现用户指定的n个阶乘
def factorial():
    # 步骤1：接受用户输入的一个数字
    n = int(input('\n请输入您需要计算的阶乘数据：>'))
    # 步骤2：设置第1项的初始值
    factorial = 1
    # 步骤3：判断输入是否合法（n值>=0）
    if n < 0:
        print('提示：负数没有阶乘\a')
        pass
    elif n == 0:
        # 若数字为0，则值为1
        print('0! = {0}'.format(factorial))
        pass
    else:
        # 使用for循环计算阶乘结果
        for i in range(1, n + 1):
            factorial *= i  # 计算
            pass
        # 输出结果
        print('结成数据为：', '{0}! = {1}'.format(n, factorial))
        pass


# 16.两个英语单词的列表中有，有几个重复的元素
def strabc():
    while True:
        a = str(input('请输入单词A：'))
        b = str(input('请输入单词B：'))
        n = 0
        # noinspection PyBroadException
        try:
            for i in range(len(a)):
                if a[i - n:i + 1] in b:
                    n += 1
            return n
        except:
            break


if __name__ == '__main__':
    # bubble_sort()  # 1 .冒泡算法
    selection_sort()  # 2. 选择排序
    # insertion_sort()  # 3 .插入排序
    # shell_sort()  # 4. 希尔排序
    # print('归并排序一：', merge_sort_1(ls))  # 5-1. 归并排序一
    # new_list = merge_sort_2(ls)
    # for k, v in enumerate(new_list):
    #     ls[k] = v
    # print('归并排序二：', ls)  # 5-2. 归并排序二
    # prime_number()  # 6.100以内的质数
    # selection_word()  # 7. 找出一段英文句子的最长的一个单词
    # multiplication_table_for()  # 9-1. 99乘法表for-for语句
    # multiplication_table_while()  # 9-2. 99乘法表while-while语句
    # comprehensions()  # 9-3 99乘法表列表推导式
    # distences_time()  # 10-1.求已知时间的时间差
    # time_times()  # 10-2.求时间差
    # stra()  # 11.列表逆序
    # matrix_transposed()  # 12.Matrix transposed（矩阵转置），嵌套列表推导式（解析式）
    # fibonacci_while_01()  # 13-1.Fibonacci sequence（斐波那契数列）,使用while循环实现对位换值方式
    # fibonacci_while_02()  # 13-2.While循环的实现
    # fibonacci_for()  # 13-3.for循环实现的方法
    # armstrong()  # 14.Armstrong number（阿姆斯特朗数），使用Python3实现数值用户指定范围的阿姆斯特朗数
    # factorial()  # 15.Factorial（阶乘），使用Python3实现用户指定的n个阶乘
    # print('重复元素的个数为：', strabc())  # 16. 两个英语单词的列表中有几个重复的元素
