import pytesseract, os
import numpy as np
import matplotlib.pyplot as plt
import os.path
from cnocr import CnOcr
from PIL import Image
from pdf2docx import Converter

def readTextInPicture():
    ocr = CnOcr()
    res = ocr.ocr(r'H:\pictures\04.png')
    print('Predicted Chars:', res)

    image = Image.open(r'H:\pictures\04.png')
    code = pytesseract.image_to_string(image, lang='eng')
    print('识别的文字为：', code)


# 1，使用PLT,Matplotlib,Numpy对模糊老照片进行修复
# 读取图片
img_path = 'H:\\pictures\\05.jpg'
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


def repairThePhotos():
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


# 2，PDF装换为Word文件
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


if __name__ == '__main__':
    # readTextInPicture()
    repairThePhotos()
    # pdfToWord()
