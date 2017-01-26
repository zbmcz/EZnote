#coding=utf-8

# 显示变量的类型
a = 1.12
type(a)

# 查看python的关键字
#inport keyword
#keyword.kwlist

# python的输出
age = 22
name = 'Giraffe'
print("我的名字是%s，我的年龄是%d"%(name,age))

# python的输入
password = raw_input("请输入密码")
print '您刚刚输入的密码是:',password

# python的for循环
mstr = "hello-python"
for x in mstr:
	print(x)
else:
	print("没有数据")

# 字符串的下标
xstr = "hello"
print(xstr[0])

# 字符串的切片 print(起点下标:终点下标前一位:步长)
qstr = "hello"
print(qstr[0:3])
print(qstr[2:]) #从下标为2的字符开始到最后的字符

# 列表的插入
mlb = ["aaa","bbb"]
mlb.append("ccc")
mlb_ = ["ddd","eee"]
mlb.extend( mlb_ )
mlb.insert(0,"first")
print(mlb)

# 列表的查找
dlb = ["aaa","bbb","ccc"]
if "aaa" in dlb:
	print("找到了")
else:
	print("没有找到")

# 列表的删除
slb = ["x","aaa","bbb"]
del slb[0]

slb_ = ["aaa","bbb","x"]
slb_.pop()

_slb = ["aaa","x","bbb"]
_slb.remove('x')

#列表的遍历
print "列表的遍历"
blb = ["aaa","bbb","ccc"]
for e in blb:
	print e

# 元组
# 即不能修改的列表
myz = ("aa",12,32)

# 字典的应用

# 修改全局变量
qj = 100
def changeGlobal():
	global qj
	print('修改前 qj=%d'%qj)
	qj = 200
	print('修改后 qj=%d'%qj)
def showGlobal():
	print('现在的 qj=%d'%qj)
changeGlobal()
showGlobal()


# 函数的缺省参数
def printInfo( name , age = 35 ):
	print "Name: ",name
	print "Age: ",age
printInfo( name="Old Giraffe" )
printInfo( age = 21, name="Giraffe" )

# 函数的多返回值
# 本质是利用了元组
print "函数的多返回值"
def dfhfunction():
	year = 2017
	month = 1
	return year,month
y,m = dfhfunction()
print "y = ",y
print "m = ",m

# 不定长参数
def bdcfunction(a,b, *args , **kwargs):
	print "a = ",a
	print "b = ",b
	print "args = ",args
	print "kwargs : "
	for key,value in kwargs.items():
		print key, "=",value
bdcfunction(1,2,3,4,5,m=6,n=7,p=8)

# 匿名函数
getSum = lambda a,b : a + b
print "5 + 6 = ", getSum(5,6)

# 匿名函数的应用
print "匿名函数的应用"
def nmfunction(a,b,opt):
	print "a = ",a
	print "b = ",b
	print "result = ",opt(a,b)
nmfunction(1,2, lambda x,y:x+y)


