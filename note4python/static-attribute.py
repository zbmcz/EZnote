#coding=utf-8

class People(object):

	address = '天津'  # 公有的类属性
	__school = '河北工业大学' # 私有的类属性

	def __init__(self):
		self.name = '小明' # 实例属性
		self.age = 18 # 实例属性
		self.__sex = '男' # 私有的实例属性

		# 实例属性会屏蔽掉同名的类属性
		# self.address = '河北'
		# p = People()
		# p.address 为 '河北'
	
print People.address

