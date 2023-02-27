# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:11:28 2023

@author: Krithika
"""

import sympy as sp
'''n=int(input("Enter number of values:"))
x=[]
fx=[]

for i in range(n):
  x.append(float(input("Enter x:")))
  fx.append(float(input("Enter f(x):")))
'''
n=7
x=[3,4,5,6,7,8,9]
fx=[4.8,8.4,14.5,23.6,36.2,52.8,73.9]
table=[]
table.append(fx)

h=x[1]-x[0]
for i in range(n-1):
  t=[]
  for j in range(len(table[i])-1):
    t.append((table[i][j+1]-table[i][j])/(x[j+1+i]-x[j]))
  table.append(t)
b=[]
for i in range(len(table)):
  b.append(table[i][0])
def ch(n):
  if n>=0:
    return '+'
  else:
    return '-'
def fac(n):
    if n==1:
        return 1
    else:
        return (n*fac(n-1))
result=str(b[0])
value=b[0]

for i in range(1,n):
  result+=" %c %.2f"%(ch(b[i]),(b[i]))
  for j in range(i):
    result+="*(x %c %.2f)/%.2f"%(ch(-x[j]),abs(x[j]),fac(i))

polynomial=result

p=sp.symbols('x')
dydx=sp.Derivative(result,p).doit()
d2ydx2=sp.Derivative(result,p).doit()

X=input("\nEnter x for which the value of the function has to be found:")
dydx = str(dydx).replace("x",str((float(X)-x[0])/h))
print("\ndy/dx at %s = %.3f"%(X,eval(dydx)/h))

X=input("\nEnter x for which the value of the function has to be found:")
d2ydx2 = str(d2ydx2).replace("x",str((float(X)-x[0])/h))
print("\nd2y/dx2 at %s = %.3f"%(X,eval(d2ydx2)/h**2))

 #---------------------------------------------------

#integral using simpson's 1/3 rule
from math import *

'''a=float(input("Enter the lower limit of the integral:"))
b=float(input("Enter the upper limit of the integral:"))
fx=input("Enter the function of x:")
n=int(input("Enter the value of n:"))'''

a=4
b=5.2
fx="log(x)"
n=10


def f(x):
  return eval(fx.replace('x',str(x)))

x=[]
y=[]
h=(b-a)/n
for i in range(n+1):
  x.append(a+i*h)
  y.append(f(x[i]))

r1=r2=0

for i in range(1,n):
  if i%2==0:
    r2+=y[i]
  else:
    r1+=y[i]


print("Interal %s from %.2f to %.2f : %.2f"%(fx,a,b,h/3*(y[0]+y[n]+4*r1+2*r2)))

#-----------------------------------------

#integral using simpson's 3/8 rule
from math import *

'''a=float(input("Enter the lower limit of the integral:"))
b=float(input("Enter the upper limit of the integral:"))
fx=input("Enter the function of x:")
n=int(input("Enter the value of n:"))'''

a=4
b=5.2
fx="log(x)"
n=10


def f(x):
  return eval(fx.replace('x',str(x)))

x=[]
y=[]
h=(b-a)/n
for i in range(n+1):
  x.append(a+i*h)
  y.append(f(x[i]))

r1=r2=0

for i in range(1,n):
  if i%3==0:
    r2+=y[i]
  else:
    r1+=y[i]


print("Interal %s from %.2f to %.2f : %.2f"%(fx,a,b,3*h/8*(y[0]+y[n]+3*r1+2*r2)))

#-------------------------------------------
#train question



'''n=int(input("Enter the number of time intervals:"))
t=[]
v=[]

for i in range(n):
  t.append("Enter the time:")
  v.append("Enter the velocity at this time:")'''

n=9
t=[0,5,10,15,20,25,30,35,40]
v=[30,24,19.5,16,13.6,11.7,10,8.55,7]

a=t[0]
b=t[-1]
h=(b-a)/(n+1)


print("Using Trapezoidal Rule:\n")
print("Distance moved by the train from 0 to 40 secs : %.2f"%((2*sum(v)-v[0]-v[-1])*h/2))

r1=r2=0

for i in range(1,n):
  if i%3==0:
    r2+=y[i]
  else:
    r1+=y[i]

print("\n\nUsing Simpson's One Third Rule:\n")
print("Distance moved by the train from 0 to 40 secs : %.2f"%(h/3*(v[0]+v[-1]+4*r1+2*r2)))

r1=r2=0

for i in range(1,n):
  if i%3==0:
    r2+=y[i]
  else:
    r1+=y[i]

print("\n\nUsing Simpson's Three Eight Rule:\n")
print("Distance moved by the train from 0 to 40 secs : %.2f"%(3*h/8*(v[0]+v[-1]+3*r1+2*r2)))
