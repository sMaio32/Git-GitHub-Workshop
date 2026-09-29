#Sonny Maiorino
#5-28-2026
#Template for Graphing a Function

import numpy as np
import matplotlib.pyplot as plt

#insert your function here
def f(x, a, b, c):
    return a*x**2 + b*x + c

def z(x, a, b):
    return a*np.sin(b*x)

#setting your x and y
xlist = np.linspace(0,3,num=1000)
sinxlist = np.linspace(0,19,num=1000)
ylist = f(xlist, 2, 1, -3)
zlist = z(sinxlist, 3, 0.5)

#format graph
plt.figure(num=0, dpi = 120)
plt.plot(xlist, ylist, label="f(x) = 2x$^2$ + x -3") #graph x and y, can do LaTeX formatting for label
plt.plot(ylist, xlist, "--r", label = "f$^{-1}$(x)") #graphs inverse, '--r' is red dotted line
plt.plot(sinxlist, zlist, "g", label = "z(x) = 3sin(0.5x)") #graphs sinx function
plt.title("What You're Graphin")
plt.xlabel("Independent Var (Units)")
plt.ylabel("Dependent Var (Units)")
plt.legend()
plt.show()
