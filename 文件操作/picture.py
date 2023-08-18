import cv2
import pytesseract, os
import numpy as np
import matplotlib.pyplot as plt
import os.path
from cnocr import CnOcr
from PIL import Image

img_ocr = r'H:\pictures\04.png'
img_path = 'H:\\pictures\\05.jpg'
img_file = 'H:\\pictures\\06.jpg'
img_newfile = 'H:\\pictures\\07.jpg'


# 1，识别图片文字
def read_text_in_picture():
    ocr = CnOcr()
    res = ocr.ocr(img_ocr)
    print('Predicted Chars:', res)

    image = Image.open(r'H:\pictures\04.png')
    code = pytesseract.image_to_string(image, lang='eng')
    print('识别的文字为：', code)


# 2，使用PLT,Matplotlib,Numpy对模糊老照片进行修复
# 读取图片

img = Image.open(img_path)

# 图片转化为numpy数组
img = np.asarray(img)
flat = img.flatten()


# 创建函数
def get_histogram(image, bins):
    histogram = np.zeros(bins)
    for pixel in image:
        histogram[pixel] += 1
    return histogram


def repair_the_photos():
    hist = get_histogram(flat, 256)
    cs = np.cumsum(hist)
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()
    cs = nj / N
    cs = cs.astype('uint8')
    img_new = cs[flat]
    img_new = np.reshape(img_new, img.shape)
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    # fig.add_subplot(1, 2, 1)
    # plt.imshow(img, cmap='gray')
    # plt.title("Image 'Before' Contrast Adjustment")
    fig.add_subplot(1, 1, 1)
    plt.imshow(img, cmap='gray')
    # plt.title("Image 'After' Contrast Adjustment")
    filename = os.path.basename(img_path)
    plt.show()
    pass


# 3，更换证件照背景
'''
img=cv2.imread(img_file,0)
kernel=np.ones((5,5),np.uint8)
print(kernel)
#腐蚀
erosion=cv2.erode(img,kernel)
#膨胀
dilation=cv2.dilate(img,kernel)
cv2.imshow('erosion/dilation',np.hstack((img,erosion,dilation)))
cv2.waitKey(0)  #展示照片中无限期等待
'''


def photos_change_background_color():
    # 图片导入
    img = cv2.imread(img_file)
    # 图片缩放
    rows, cols, channels = img.shape
    print(rows, cols, channels)
    img = cv2.resize(img, None, fx=1, fy=1)  # 图片缩小为原来的一半
    rows, cols, channels = img.shape
    print(rows, cols, channels)
    # 显示图片内容
    cv2.imshow('img', img)
    '''
    # 转化成二值化图像
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)
    lower_blue = np.array([50, 50, 50])
    upper_blue = np.array([110, 255, 255])

    # 实现二值化功能
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    cv2.imshow('mask', mask)
'''

    # 转换成灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 中值滤波去除噪声
    median = cv2.medianBlur(gray, 3)
    # 图像直方图均衡化
    equalize = cv2.equalizeHist(median)
    # Sobel 算子锐化处理
    sobel = cv2.Sobel(median, cv2.CV_8U, 1, 0, ksize=7)
    # 图像二值化处理
    ret, binary = cv2.threshold(sobel, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    # 显示图像
    cv2.imshow(img_newfile, binary)
    cv2.waitKey(0)

    '''
    # 腐蚀
    erosion = cv2.erode(mask, None, iterations=1)
    cv2.imshow('erosion', erosion)
    # 膨胀
    dilation = cv2.dilate(mask, None, iterations=1)
    cv2.imshow('dilation', dilation)
    for i in range(rows):
        for j in range(cols):
            if erosion[i, j] == 255:
                img[i, j] = (219,142,67)#蓝底RGB(67, 142, 219)BGR(219,142,67)照片        红色RGB(255, 0, 0)BGR(0,0,255)
    cv2.imshow('res', img)
    cv2.imwrite(img_newfile,img)
    '''
    cv2.waitKey(0)  # 展示照片中无限期等待

    # 销毁所有窗口
    cv2.destroyAllWindows()


from PIL import Image


def change_background_color(image_path, new_color):
    # 打开图像
    image = Image.open(image_path)

    # 将图像转换为RGBA模式
    image = image.convert("RGBA")

    # 获取图像的宽度和高度
    width, height = image.size

    # 创建一个新的空白图像，底色为指定的颜色
    new_image = Image.new("RGBA", (width, height), new_color)

    # 将原始图像粘贴到新图像上
    new_image.paste(image, (0, 0), image)

    # 保存修改后的图像
    new_image.save("H:\\pictures\\modified_image.png")


import cv2
import numpy as np


def picture():
    # 读取照片
    image = cv2.imread(img_file)
    # 修改尺寸
    image = cv2.resize(image, None, fx=0.5, fy=0.5)
    # 图片转换为二值化图
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # print(hsv)
    # 图片的二值化黑白处理
    lower_red = np.array([110, 70, 150])
    upper_red = np.array([150, 255, 255])
    heibai = cv2.inRange(hsv, lower_red, upper_red)

    # 闭运算
    k = np.ones((5, 5), np.uint8)
    r = cv2.morphologyEx(heibai, cv2.MORPH_CLOSE, k)
    # 原图显示
    cv2.imshow('image', image)
    # 颜色替换
    rows, cols, channels = image.shape
    for i in range(rows):
        for j in range(cols):
            if r[i, j] == 255:  # 像素点为255表示的是白色，我们就是要将白色处的像素点，替换为红色
                image[i, j] = (219, 142, 67)  # 此处替换颜色，为BGR通道，不是RGB通道
    # 新图显示
    cv2.imshow('red', image)
    # 无限等待
    cv2.waitKey(0)
    # 销毁内存
    cv2.destroyAllWindows()
    # 新图保存
    cv2.imwrite('H:\\pictures\\redzhengjian.jpg', image)


import os
import argparse

import numpy as np
import cv2 as cv


# 对证件照进行三种颜色的换底操作
def change_color(image_path, output_path):
    # 读入数据
    image = cv.imread(image_path)

    h, w, ch = image.shape

    data = image.reshape((-1, 3))
    # 数据转换，计算更快
    data = np.float32(data)

    # 设置聚类
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    num_clusters = 4
    # label就是各个像素点的所属的类别标签，通常第一个像素点的标签就是背景色的标签
    _, label, _ = cv.kmeans(data, num_clusters, None, criteria, num_clusters, cv.KMEANS_RANDOM_CENTERS)

    # 找到背景像素的类别
    indx = label[0][0]

    # 生成掩膜
    mask = np.ones((h, w), dtype=np.uint8) * 255
    label = np.reshape(label, (h, w))

    mask[label == indx] = 0

    # 处理掩膜，使得生成的图像更加完美
    se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    cv.erode(mask, se, mask)
    mask = cv.GaussianBlur(mask, (5, 5), 0)

    # 白色背景[255, 255, 255]
    bg_w = np.ones(image.shape, dtype=np.float) * 255

    # 红色背景 注意：opencv中的像素三通道的排列顺序为BGR，而非RGB。所以红色为[0, 0, 255]， 蓝色为[255, 0, 0]
    red = np.array([0, 0, 255])
    bg_r = np.tile(red, (h, w, 1))

    # 蓝色背景
    blue = np.array([255, 0, 0])
    bg_b = np.tile(blue, (h, w, 1))

    # alpha 即为需要保留的部分，则 1-alpha 为要去除的背景，此处可以看作两张图像的加权融合
    alpha = mask.astype(np.float32) / 255
    fg = alpha[..., None] * image
    bg = 1 - alpha[..., None]
    new_image_white = fg + bg * bg_w
    new_image_red = fg + bg * bg_r
    new_image_blue = fg + bg * bg_b

    # 保存图片
    w_path = os.path.join(output_path, 'white.jpg')
    r_path = os.path.join(output_path, 'red.jpg')
    b_path = os.path.join(output_path, 'blue.jpg')

    cv.imwrite(w_path, new_image_white.astype(np.uint8))
    cv.imwrite(r_path, new_image_red.astype(np.uint8))
    cv.imwrite(b_path, new_image_blue.astype(np.uint8))

    print('OK done!')


if __name__ == '__main__':
    # read_text_in_picture()
    # repair_the_photos()
    # photos_change_background_color()
    # change_background_color(img_newfile,(0, 0, 255,255))
    # picture()
    '''
    # ap = argparse.ArgumentParser()
    # ap.add_argument('-i', '--image', default='./image.jpg', help='path to the input image.')
    # ap.add_argument('-p', '--path', default='.', help='path to the output image.')
    # args = vars(ap.parse_args())
    '''

    change_color(img_file, 'H:\\pictures\\')
    pass
