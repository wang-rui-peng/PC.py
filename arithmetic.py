import time
import math

ls = [70, 15, 52, 55, 82, 3, 40, 17, 90, 1, 100, 23]

# 1 冒泡算法
for i in range(len(ls) - 1):
    for j in range(len(ls) - 1 - i):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
print("冒泡结果为：", ls)
print("--" * 30)
pass

# 2 选择排序
for i in range(len(ls) - 1):
    # 记录最小数的索引
    minIndex = i
    for j in range(i + 1, len(ls)):
        if ls[j] < ls[minIndex]:
            minIndex = j
    # i 不是最小数时，将 i 和最小数进行交换
    if i != minIndex:
        ls[i], ls[minIndex] = ls[minIndex], ls[i]
print("选择结果为", ls)
print("--" * 30)
pass

# 3 插入排序
for i in range(len(ls)):
    preIndex = i - 1
    current = ls[i]
    while preIndex >= 0 and ls[preIndex] > current:
        ls[preIndex + 1] = ls[preIndex]
        preIndex -= 1
    ls[preIndex + 1] = current
print("插入结果为：", ls)
print("--" * 30)
pass

# 4 希尔排序

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
print("--" * 30)
pass


# 归并排序
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


# 归并排序
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


# 1.求已知时间的时间差
import datetime


def distences_time():
    start_time = '2022-09-07 19:30:00'
    end_time = '2022-09-07 19:37:00'
    start_time_str = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time_str = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    sec = (end_time_str - start_time_str).seconds
    print('两个时间点的时间差为：', sec)


# 2.100以内的质数
a = []
for num in range(2, 100):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        a.append(num)
print('100以内的质数为：', a)

# 找出一段英文句子的最长的一个单词
import re

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

# 1-9的平方和
print('1-9的平方和为：', sum(i ** 2 for i in range(0, 10)))

# 99乘法表for-for语句
for i in range(0, 10):
    for j in range(1, i + 1):
        print('{}*{}={}'.format(j, i, j * i), end=' ')
    print('')

# 99乘法表while-while语句
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i * j}', end=' ')
        j += 1
    print('')
    i += 1

# 99乘法表列表推导式
print('------------------------------')
print('99乘法表为：',
      '\n'.join([' '.join(['%2s * %s = %2s' % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))


# 求时间差
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


# 两个英语单词的列表中有，有几个重复的元素
def strabc():
    while True:
        a = str(input())
        b = str(input())
        n = 0
        # noinspection PyBroadException
        try:
            for i in range(len(a)):
                if a[i - n:i + 1] in b:
                    n += 1
            return n
        except:
            break


# 列表逆序
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def stra():
    print('列表逆序结果为：', a[::-1])
    a.reverse()
    print('列表逆序结果为：', a)
    print('列表逆序结果为：', list(reversed(a)))


if __name__ == '__main__':
    print('归并排序1')
    print('ls:', merge_sort_1(ls))

    print('归并排序2')
    new_list = merge_sort_2(ls)
    for k, v in enumerate(new_list):
        ls[k] = v
    print('ls:', ls)

    distences_time()

    time_times()
    # print(strabc())
    stra()
