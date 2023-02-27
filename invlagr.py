# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:33:05 2023

@author: 21pd19
"""

class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# Function to calculate
# the inverse interpolation
def inv_interpolate(d: list, n: int,
                    y: float) -> float:
 
    # Initialize final x
    x = 0
 
    for i in range(n):
 
        # Calculate each term
        # of the given formula
        xi = d[i].x
        for j in range(n):
            if j != i:
                xi = (xi * (y - d[j].y) /
                      (d[i].y - d[j].y))
 
        # Add term to final result
        x += xi
    return x
 
# Driver Code
if __name__ == "__main__":
 
    # Sample dataset of 4 points
    # Here we find the value
    # of x when y = 4.5
    d = [Data(1.2,4.2),
         Data(2.1,6.8),
         Data(2.8,9.8),
         Data(4.1,13.4),
         Data(4.9,15.5),
         Data(6.2,19.6)]
 
    # Size of dataset
    n = 6
 
    # Sample y value
    y = 12
 
    # Using the Inverse Interpolation
    # function to find the
    # value of x when y = 4.5
    print("Value of x at y = 12 :",
           round(inv_interpolate(d, n, y), 5))