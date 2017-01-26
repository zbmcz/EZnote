#coding=utf-8

def function1(a):
	a += a
a_int = 1
a_list = [1,2]
print "before function1 a_int = ",a_int
print "before function1 a_list = ",a_list
function1(a_int)
function1(a_list)
print "after function1 a_int = ",a_int
print "after function1 a_list = ",a_list

def function2(b):
	b = b + b
b_int = 1
b_list = [1,2]
print "before function2 b_int = ",b_int
print "before function2 b_list = ",b_list
function2(b_int)
function2(b_list)
print "after function2 b_int = ",b_int
print "after function2 b_list = ",b_list
