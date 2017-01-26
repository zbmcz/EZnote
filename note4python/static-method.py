#coding=utf-8

class People(object):
	
	country = 'china'
	address = '天津'

	# 类方法 用classmethod来进行修饰
	@classmethod
	def getCountry(cls):
		return cls.country
	
	@classmethod
	def setCountry(cls,country):
		cls.country = country
	
	# 静态方法 用staticmethod进行修饰 第一个参数不必强制
	@staticmethod
	def getAddress():
		return People.address
	
	@staticmethod
	def setAddress(address):
		People.address = address
