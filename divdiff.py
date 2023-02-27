import math
import sympy as sp
# Function to find the product term
def proterm(i, value, x):
    pro = 1;
    for j in range(i):
        pro = pro * (value - x[j]);
    return pro
 
# Function for calculating
# divided difference table
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /(x[j] - x[i + j]))
    return y
 
# Function for applying Newton's
# divided difference formula
def applyFormula(value, x, y, n):
 
    sum = y[0][0];
 
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]);
     
    return sum
 
# Function for displaying divided
# difference table
def printDiffTable(y, n):
 
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t",
                               end = " ")
 
        print("")
 
# Driver Code
 
i = 0

x = [] 
y=[]
n = int(input("\nEnter the number of Variables : "))



print("Enter the Values : ")
for i in range(0, n):
    
    dummy = float(input())
    x.append(dummy)

y = [[0 for i in range(n+1)] for j in range(n)]
    
print("Enter the f(x) values respetively : ")
for i in range(0, n):

    dummy = float(input())
    y[i][0] = dummy

   

#choice = input("Is the value to find for in exponential ? If yes Press Y/y else Press N/n ")
value = float(input("Enter the value to find for : "))

fin_ans=[]
fin_ans.append(y[0])
j=n
for i in range(n-1):
    temp=[]
    for z in range(j-1):
        diff=(y[z+1]-y[z])/(x[i+z+1]-x[z])
        temp.append(diff)
    if(temp!=[]):
        fin_ans.append(temp[0])
    y=temp
    j-=1

res=fin_ans[0]
a=sp.Symbol('x')
m=1
for i in range(1,n):
    m*=(a-x[i-1])
    res+=(m*fin_ans[i])

print(res)

# to check for exp input
"""
if choice == 'Y' or choice =='y':
    value = float(input("Enter the power of the exponent : "))
    value = math.exp(value)
elif choice == 'N' or choice =='n':
    value = float(input("Enter the value to find for : "))
"""
y = dividedDiffTable(x, y, n)

print("\nDivided Difference Table : \n")
printDiffTable(y, n)
 
print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 4))