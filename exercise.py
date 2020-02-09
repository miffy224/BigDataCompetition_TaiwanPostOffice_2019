"""
***Introduction to Python***
"""


#lesson: for
"""
list=[1,5,2,5,88 ]
for i in list:
	print i
	print "in "
"""
#lesson: range(1,3)will only print 1,2

"""
for i in range(1,10):
	print i
"""

#lesson: range(1,10,5)will only print 1,6(because step=5)
"""
for i in range(1,10,5):
	print i
"""

#lesson: if (almost same as C)
"""
a = 1
b = 2
c = 3
if a<c>b:
	print "c is the largest one" 
"""
#lesson: if else
"""
a = 1
b = 2
if a<b:
	print "b is larger" 
else: #":"is needed
	print "b is smaller"
"""

#lesson: if elif else
"""
a = 1
if a<1:
	print "a<1" 
elif a==1: #":"is needed
	print "a=1"
else:
	print "a>1"
"""

#lesson: def function
"""
def a():
	print "this is a function"
	b=1+2
	print b

a() #call the function
"""

#lesson: function parameter
"""
def fun1(a,b=1,c="pig",d=True):
	print 'a:', a,'b:', b,'c:', c,'d:', d
fun1(4)
"""

#lesson: local & global
"""
APPLE = 100
a = 10 #still need to define outside the function
def fun():
	global a
	a = 20
	return a+APPLE

print a
print fun()
"""


