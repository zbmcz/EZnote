#coding=utf-8
class People(object):

		def __init__(self,start):
			self.count = start

		def __iter__(self):
			return self

		def next(self):
			if self.count <= 0 :
				raise StopIteration
			r = self.count
			self.count -= 1
			return r

for item in People(10):
	print item