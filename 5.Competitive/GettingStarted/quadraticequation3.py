"""
solving the quadratic equation
"""
import math
def solveequationss(a,b,c):
    num=float(b*b-4*a*c);
    dis=math.sqrt(num)
    if dis==0.0:
        print("The equation have unique and equal root")
        print(f'root1=root2={-b/(2*a)}\n')
    elif dis>0.0:
        print("The equation has the unique and the unequal roots")
        print(f'root1={(-b+dis)/(2*a)}\nroot2={(-b-dis)/(2*a)}')
    else:
        print("The Equation has the complex root")


if __name__ == '__main__':
    try:

        print()
        print("Equation:ax^2+bx+c=0..")
        a = int(input("Enter the co-efficient of x^2 (The value of a) ->"))
        b = int(input("Enter the co-efficient of x (The value of b) _>"))
        c = int(input("Enter the constant term (The value of c) ->"))
        print(f"\nCheck the equation is it correct or not\n{a}X^2+{b}X+{c}")
        solveequationss(a, b, c)
    except Exception as e:
        print(e)