#coding=utf-8

import urllib

f = urllib.urlopen("http://www.hebut.edu.cn")

html = f.read()

print(html)

