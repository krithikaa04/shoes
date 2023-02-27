def trapezoidal(t,v,n):
    h = 5
    integration = v[0] + v[len(t)-1]
    
    for i in range(1,n):   
        integration = integration + 2 * v[i]    
    integration = integration * h/2
    
    return integration


def simpsons_1by3(t,v,n): 
    h = 5
    x = t
    fx = v
    i = 0
    res = 0
    i = 0
    for i in range(n):
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    
    res = res * (h / 3)
    return res

def simpsons_3by8(t,v,n):    
    h = 5
    sum_ = v[0]+v[len(v)-1]
    for i in range(1, len(v) ):
        if (i % 3 == 0):
            sum_ = sum_ + 2*v[i]
            
        else:
            sum_ = sum_ + 3*v[i]

    return ((float( 3 * h) / 8 ) * sum_ )



t = [0,5,10,15,20,25,30,35,40]
v = [30,24,19.5,16,13.6,11.7,10.0,8.5,7.0]

n = len(t)
print("Distance teavelled in meters by trapezoidal rule : ",trapezoidal(t,v,n)," meters")
print("Distance teavelled in meters by Simpson's 3/8 rule : ",simpsons_3by8(t,v,n)," meters")
print("Distance teavelled in meters by Simpson's 1/3 rule : ",simpsons_1by3(t,v,n)," meters")

