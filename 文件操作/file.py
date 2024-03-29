import os
import os.path
from pdf2docx import Converter

# 1，PDF装换为Word文件
def pdfToWord():
    pdf = input("Enter the path to your file:")
    assert os.path.exists(pdf), "File not found at," + str(pdf)
    f = open(pdf, 'r+')
    doc_name_choice = input("Do you want to give a custom name to your file ?(Y/N)")
    if (doc_name_choice == 'Y' or doc_name_choice == 'y'):
        doc_name = input("Enter the custom name :") + ".docx"
    else:
        pdf_name = os.path.basename(pdf)
        doc_name = os.path.splitext(pdf_name)[0] + ".docx"

    cv = Converter(pdf)
    path = os.path.dirname(pdf)
    cv.convert(os.path.join(path, "", doc_name), start=0, end=None)
    print("Word doc created!")
    cv.close()
    pass


# 2.多线程操作大文件
def readTimes():
    if os.path.exists(r'/python.log'):
        print('文件已存在！')
        with open('python.log', 'r+') as file:
            file.truncate(0)
            print('文件中的内容已清空。')
    else:
        # os.path.join('python'+'.log')
        file = os.getcwd()
        open('python.log', 'w')
        print(file)
        print('文件已创建成功！')
    filerDir = os.path.join(os.getcwd(), '/')
    print(filerDir)
    with open(filerDir + os.sep + 'python.txt', 'r+', encoding='utf8') as fp:
        content = fp.read()
        # print(fp.seek(2))
        print(content)
        with open(filerDir + os.sep + 'python.log', 'w', encoding='utf8') as writeText:
            for i in content:
                writeText.write(i)
            print('文件写入完毕！')
            writeText.close()


filerpath1 = r'D:\python\PC\python.txt'
filerpath2 = r'D:\python\PC\python.docx'


def readAndWrite():
    # with open(filerpath1,'r') as f:
    #     content=f.readlines()
    #     print('目标文件的内容为：{}'.format(content))
    #     with open(filerpath2,'a+') as f1:
    #         for i in content:
    #             f1.write(i)
    ms = open(r'/python.txt', encoding='utf-8', errors='ignore')
    for line in ms.readlines():
        with open(r'/python.log', 'a') as fp:
            fp.write(line)


def toBigFile():
    with open('my_file', 'wb') as f:
        num_chars = 1024 * 1024 * 1024
        f.write('1'.encode() * num_chars)


def howMangNumber():  # 列表中某个数字的个数
    a = ['python', 'is', 'easy']
    print(' '.join(a))

    b = [1, 3, 4, 7, 8, 9, 65, 4, 3, 2, 4, 6, 4, 54, 4, 10]
    # print(max(set(b),key=b.count))
    from collections import Counter
    cnt = Counter(b)
    print(cnt.most_common(1))


def changeFileName():  # 批量修改文件名称
    path = input('请输入文件夹路径：')
    prefix = input('请输入文件名前缀：')
    suffix = input('请输入文件名后缀：')

    # 获取该目录下所有文件，存入列表中
    fileList = os.listdir(path)
    #m = int(input('请输入开始的数字：'))  # python中input函数默认返回一个字符串，需强制转化为整数
    n = 1
    for inner_file in fileList:
        # 获取旧文件名（就是路径+文件名）
        old_name = path + os.sep + inner_file  # os.sep添加系统分隔符
        if os.path.isdir(old_name):  # 如果是目录则跳过
            continue
        # 设置新文件名
        new_name = path + os.sep + prefix + '_' + str(n) + suffix
        os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名
        n += 1
    print("共修改了", n - 1, "个文件。")


if __name__ == '__main__':
    # pdfToWord()
    # readTimes()
    # readAndWrite()
    # toBigFile()
    # howMangNumber()
    changeFileName()
    pass
