#coding=utf-8

try:
	print '--------Test1 start--------'
	# 如果文件不存在 会产生 IOError 异常
	open('ffff.txt','r')
	print '--------Test1 end----------'

	print '--------Test2 start--------'
	# 如果变量没有定义 会产生 NameError 异常
	print(num)
	print '--------Test2 end----------'

except (IOError,NameError),errorMsg :
	# 如果想通过一次except捕获多个异常可以用一个元组的方式
	print(errorMsg)

else:
	print '没有产生异常 我会被执行'

finally:
	print '我一定会被执行'
