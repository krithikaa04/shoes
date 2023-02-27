# Program by Sanjay Ram RR - 21PD32

x0 = float(input("Enter the Value of x0 : "))
x1 = float(input("Enter the Value of x1 : "))
x2 = float(input("Enter the Value of x2 : "))


f0 = float(input("Enter the Value of f(x0) : "))
f1 = float(input("Enter the Value of f(x1) : "))
f2 = float(input("Enter the Value of f(x2) : "))


x = float(input("Enter the value to find for : "))

#-------------------------------------------------------------------------

# Result

#-------------------------------------------------------------------------

b0 = f0
b1 = ( (f1 - f0) / (x1 - x0) )
b2 = ( ( (f2 - f1) / (x2 - x1) ) - ( (f1 - f0) / (x1 - x0) ) ) / (x2 - x0)

fx = b0 + ( b1 * (x - x0)) + (b2 * (x - x0) * (x - x1) )

temp = ( (f1 - f0) / (x1 - x0) )

print("#-----------------------------------------------------------------")
print("\n")

print("b0 = %0.5f" % b0)
print("b1 = %0.5f" % b1)
print("b2 = %0.5f" % b2)

print("\n\nThe Interpolated value at the given point : %0.5f" % fx)
print("\nQuadratic Polynomial :\nf(x) = " + str(round(b0,3)) + " + " + str(round(b1,3)) + " * (x - " + str(x0) + ") + " + str(round(b2,3)) + " * (x - " + str(x0) + ") * (x - " + str(x1) + ")")

print("#-----------------------------------------------------------------\n")

#-------------------------------------------------------------------------