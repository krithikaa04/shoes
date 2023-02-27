# Program by Sanjay Ram RR - 21PD32

x0 = float(input("Enter the Value of lower limit of the interval (x0) : "))
x1 = float(input("Enter the Value of upper limit of the interval (x1) : "))

f0 = float(input("Enter the Value of f(x0) : "))
f1 = float(input("Enter the Value of f(x1) : "))

x = float(input("Enter the value to find for : "))

#-------------------------------------------------------------------------

# Result

#-------------------------------------------------------------------------

fx = 0
fx = ( ( (f1 - f0) / (x1 - x0) ) * (x - x0) ) + f0

temp = ( (f1 - f0) / (x1 - x0) )

print("#-----------------------------------------------------------------")

print("\n\nThe Interpolated value at the given point : %0.5f" % fx)
print("\nLinear Equation :\nf(x) = " + str(f0) + " + " + str(round(temp, 2)) + " * (x - " + str(x0) + ")")          

print("#-----------------------------------------------------------------\n")

#-------------------------------------------------------------------------