# Program by Sanjay Ram RR - 21PD32

x0 = 0
x1 = 1
x2 = 2


f0 = 0
f1 = 1
f2 = 20


#-------------------------------------------------------------------------

# Result

#-------------------------------------------------------------------------

b0 = f0
b1 = ( (f1 - f0) / (x1 - x0) )
b2 = ( ( (f2 - f1) / (x2 - x1) ) - ( (f1 - f0) / (x1 - x0) ) ) / (x2 - x0)

temp = ( (f1 - f0) / (x1 - x0) )

print("#-----------------------------------------------------------------")
print("\n")

print("b0 = %0.1f" % b0)
print("b1 = %0.1f" % b1)
print("b2 = %0.1f" % b2)

print("\nQuadratic Polynomial :\nf(x) = " + str(round(b0,3)) + " + " + str(round(b1,3)) + " * (x - " + str(x0) + ") + " + str(round(b2,3)) + " * (x - " + str(x0) + ") * (x - " + str(x1) + ")")

print("#-----------------------------------------------------------------\n")

#-------------------------------------------------------------------------