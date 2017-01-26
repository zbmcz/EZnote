#coding=utf-8

class ShortInputException(Exception):
	''' 我定义的异常类 '''
	
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast
	
try:
	s = raw_input('请输入')
	if len(s) < 3:
		raise ShortInputException(len(s),3)
except EOFError:
	print '你输入了一个结束标记EOF'
except ShortInputException,x:
	print "ShortInputException:输入的长度是%d"%x.length
else:
	print "没有发生异常"
