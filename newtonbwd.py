# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:48:53 2023

@author: 21pd03
"""

# Python3 Program to interpolate using

def calc(u,n):
	temp=u
	for i in range(n):
		temp=temp*(u+i)
	return temp

# Calculating factorial of given n
def fact(n):
	f = 1
	for i in range(2,n+1):
		f=f*i
	return f

# number of values given
n=7
x=[100,150,200,250,300,350,400];

# y is used for difference

y = [[0 for i in range(n)] for j in range(n)]
y[0][0]=10.63
y[1][0]=13.03
y[2][0]=15.04
y[3][0]=16.81
y[4][0]=18.42
y[5][0] = 19.90
y[6][0] = 21.27

# Calculating the backward difference table
for i in range(1,n):
	for j in range(n-1,i-1,-1):
		y[j][i]=y[j][i-1]-y[j-1][i-1]

# Displaying the backward difference table
for i in range(n): 
    print(x[i],end="\t");
    for j in range(i+1):
        print(round(y[i][j],4),end="\t") 
    print("")

# Value to interpolate at
value = 410

# Initializing u and sum
sum = y[n-1][0]
u=(value-x[n-1])/(x[1]-x[0])
for i in range(1,n):
	sum=sum+(calc(u,i)*y[n-1][i])/fact(i)

print("\nValue at",value,"is",round(sum,4))
