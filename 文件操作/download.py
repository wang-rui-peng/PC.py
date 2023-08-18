import sys
from you_get import common as you_get
from you_get.extractors import *

# 设置下载目录
directory = 'H:\myvedio'
url = 'https://www.youtube.com/watch?v=MAXeCR7iNmU'

sys.argv = ['you-get', '--format=BD', '-o', directory, url]
you_get.main()
