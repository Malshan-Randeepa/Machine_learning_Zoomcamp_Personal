import numpy as np

#Making matrices using zeros func..
print(np.zeros(10))
#Making matrices using ones func..
print(np.ones(10))
#Making matrices using full func..
print(np.full(15,7))#in this first we have to choose size then the needed element
#When creating array with a python list
a=np.array([1.2,3.3,4.6,2.3,8.6,6.1])
print(a)
#Accessing the 4th element
print(a[3])
#changing an element
a[2]= 111
print(a)
#Using arange func. It can make elements between the range and last no is excepted
b=np.arange(1,100)
print(b)
#When using linspace it can create given no of elements in the given range
c=np.linspace(1,100,11)
print(c)