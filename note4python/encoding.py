#coding=utf-8

# 声明一个unicode对象
unicodeObj = u'你好'

# 声明一个指定编码的字节流对象
# 下面这句话utf8Obj的格式是根据.py文件头部的coding=utf-8决定的
utf8Obj = '你好'

# print函数自动检测控制台编码并将unicode对象编码后输出
# 如果在中文windows控制台 print自动将unicodeObj转换成GBK格式后输出
# 如果print输出的是字节流对象utf8Obj 此函数会按照utf8Obj对象本身的格式输出
print unicodeObj


# 关于codecs.open
# import codecs
# codecs.open('filename', encoding='utf8')

# 关于str()和unicode()方法
# 在windows控制台
def functionDeclare():
	u = u'汉'
	print('u = ' + u)
	print repr(u)
	s = u.encode('utf-8')
	print('s = ' + s)
	print repr(s)

	y = str('汉')
	print('y = ' + y)
	print repr(y)
functionDeclare()