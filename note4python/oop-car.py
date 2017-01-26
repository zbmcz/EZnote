#coding=utf-8

class Car:
	
	def __init__(self,name):
		self.__name = name
	
	def __str__(self):
		msg = "这是一辆名叫" + self.__name + "的汽车"
		return msg

	def __del__(self):
		print "这辆名叫" + self.__name + " 的汽车被删除了"
		
	def getCarName(self):
		return self.__name

	def drive(self):
		print "这辆名叫" + self.__name + "的汽车被开动了"


BMW = Car("宝马")
print(BMW)
BMW.drive()
del BMW
