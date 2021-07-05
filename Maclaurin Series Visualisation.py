from sympy import *
from sympy import lambdify, Rational, Function
from sympy.utilities.lambdify import implemented_function
from sympy.abc import x

import numpy as np
from numpy import linspace
import matplotlib.pyplot as plt
import fractions

'''
func is the input function
noOfTerms is the number of terms you want the approximation to go to
repeatingUnitA and repeatingUnitB are how often we will show the nth approximation
(It's like the nth term so for repeatingUnitA = 2 and repeatingUnitB = 1 then all the 2n+1 powers are displayed ie all the odd powers which would be good for sin(x)

eg sin(x) is an odd function so all the even powers of x are 0 so 
eg cos(x) is an even function so all the odd powers of x are 0 so 
'''


def MaclaurinSeries(func, noOfTerms, repeatingUnitA, repeatingUnitB):
    functionName = str(func)
    lamFOriginal = lambdify(x, func, modules=['numpy'])
    lamF = lambdify(x, func, modules=['numpy'])
    fMaclaurin = 0
    approximations = []

    print("\n")
    for n in range(noOfTerms-1):
        temp = diff(func, x, repeatingUnitA*n+repeatingUnitB)
        lamF = lambdify(x, temp, modules=['numpy'])
        frac = Rational(int(lamF(0)), factorial(repeatingUnitA*n+repeatingUnitB))

        fMaclaurin = fMaclaurin + x**(repeatingUnitA*n+repeatingUnitB) * frac
        approximations.append(fMaclaurin)
        print("Maclaurin series for " + functionName + " where n = " + str(repeatingUnitA*n+repeatingUnitB) + " : "  + str(approximations[n]))

    xVals = np.linspace(-10, 10, num=100)
    yVals = lamFOriginal(xVals)
    plt.plot(xVals, yVals)

    legend = ["n = " + functionName]
    for i in range(noOfTerms):
        legend.append("n = " + str(repeatingUnitA*i+repeatingUnitB))

    for i in range(noOfTerms-1):
        yVals = []
        xVals = np.linspace(-10, 10, num=100)

        f = lambdify(x, approximations[i])

        for i in range(len(xVals)):
            yVals.append(f(xVals[i]))

        plt.plot(xVals, yVals)
        plt.title("Maclaurin series for " + functionName)
        plt.grid()

    plt.legend(legend)
    axes = plt.gca()
    axes.set_xlim([-10,10])
    axes.set_ylim([-10,10])
    plt.show()


#Example: MaclaurinSeries(sin(x), 10, 2, 1)
#Example: MaclaurinSeries(cos(x), 10, 2, 0)

loop = True
while loop:
    function = input("Enter the Maclaurin Series function as shown in README.md: ")
    exec(function)
    if function == "quit":
        loop = False
