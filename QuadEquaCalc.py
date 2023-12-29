import math
import sys
from fractions import Fraction


print("Welcome to quadratic equation calculator!")
a: float = 0
b: float = 0
c: float = 0
D: float = 0
resultPlus: float = 0
resultMinus: float = 0

while(True):
    a = float(input("\nHow much is parameter a?: "))
    if(a==0):
        print("a=0, this is not a quadratic equation")
        sys.exit()
    b = float(input("How much is parameter b?: "))
    c = float(input("How much is parameter c?: "))

    D = b**2-4*a*c

    if(D<0):
        print("The given equation has no solution in R")
    elif(D==0):
        print("The given equation has one solution in R")
        resultPlus = -b/(2*a)
        print(f"Solution for x={resultPlus}")
    else:
        print("The given equation has two solutions in R")
        resultPlus = (-b+math.sqrt(D))/(2*a)
        resultMinus = (-b-math.sqrt(D))/(2*a)
        print(f"Solution for x1={resultPlus} ({str(Fraction(resultPlus))}) and x2={resultMinus} ({str(Fraction(resultMinus))})")
    
