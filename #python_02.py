#python_02
'''print ("hellow world")
a=12
print(a)
_a=239
print(_a)
_="you"
print(_)
print(type(_))
print(type(_a))
D=23+78j
print(D)
print(type(D))
N=[10,18.8,"mock",56+78j]
print(N)
print(N[-1:-3])
print(type(N))
N.insert(1,"rock")
print(N)
tap=("touch","smooth","force",10.67)
print(tap)
print(type(tap))
#set
b={65,67,55,45,46,45,"tap"}
print(type(b))
print(b)
h={223,45,67,889,9,8,65,43,35}
print(h)
y=56.89
print(type(y))
k=67.98
jk=78.78
io= k+jk
print(io)
ya=89
yb="78"
yc=int(yb)

print(ya+yc) 
yd=int(input("enter your marks : "))
print(yd)
print(type(yd))'''
'''a =int(input("enter first number : "))
b =int(input("enter second number : "))
c = a/b
print(c)
a = 69
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)

x=56
y=67
print(x>y)
print(x<y)
a = 120
b = 90
if (a<b):
    print(" a is less than b")
elif (a>b):
    print(" a is greater than b")
else:
    print(" a is equal to b ")
a=45
b=2
print(a%b)
num = int(input("Enter a number :"))
if (num%2 ==0):
    print (num, "is a even number .")
else:
    print (num, "is a odd number .")'''
#for x in  range (100):
#   print(x)
'''for y in range(101,150):
   print(y)
num=int(input("Enter a number :"))
for z in range(1,11):
   print(num*z)'''
'''num = int(input("Enter your number : "))
for i in range (1,11):
    print(num*i)'''
'''friends =["manoj","pavan","nilesh","pratik","prashant","chintu"]
for i in friends:
    print(i)'''
'''def multi (a,b):
    return a*b
print(multi(34,67))
def add(c,g):
    return c+g
print(add(45,78))
def div(s,d):
    return s/d
print(div(56,9))'''
'''add = lambda x,y:x+y
print(add(567,9075))
#oddeven = lambda 
def add():
    print(45*67*23/78)
add()
a=("hello","market",[1,2,3,4])
print(a[-1][-1])'''

'''a={0,3,1,3,2,4,5,6,7}
b={1,2,3,4,8,9}
print(a|b)
'''
'''def hello():
    print(10+12+14)

hello()

odd =lambda num: True if num%2==1 else False
print(odd(77))
print("Hello world!")'''
#print(''' Twinkle, twinkle, little star,
 #       How I wonder what you are!
  #      Up above the world so high,
   #     Like a diamond in the sky.''')
'''a_b = ("pranay")
print(a_b)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = 5
y = "is "
z = "awesome"
print(x , y + z)
x = 5
y = 10
print(x + y) 
a = 67
b = 786
print( a % b)
import sys 
l = ["happy" , 34, 46.34 ,467,355]
t = ("happy" , 34, 46.34 ,467,355)
print (sys.getsizeof(l))
print (sys.getsizeof(t))'''
 
'''
print("\"HELLO WORLD!\"")
Fruite =["apple", "banan","cherry"]
for X in Fruite:
   print(X)
   if X=='banan':
    break

for A in range(6):
  print(A)
else:
  print("finally finished!")


import pandas
print('pandas{}'.format(pandas.__version__))

import pandas as pd
data = pd.read_excel(r"C:\Users\jagta\Downloads\ACME Company Move.xlsx")'''
'''
def demo_function ():
    print("welcome to my World...")

demo_function ()
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarning("ignore")
df_csv= pd.read_csv(r"C:\Users\jagta\OneDrive\Documents\Book1.xlsx")