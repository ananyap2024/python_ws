#roots of equation (ax^2 + bx + c = 0)

import cmath

def roots(a,b,c):
    if a == b == c == 0:
            print("Infinite solutions")
    elif a == b == 0:
         print("No real roots")
         return 0
    elif a == c == 0:
         print("1 real root : 0")
         #determinant(a,b,c)
    elif b == c == 0:
         print("1 real root : 0")
         #determinant(a,b,c)
    elif a == 0:
         print("1 real root : 0")
         #determinant(a,b,c)
    elif b == 0:
         print("Imainary roots")
    elif c == 0:
        print("2 real roots")
        determinant(a,b,c)
    else:
        determinant(a,b,c)

        
def determinant(a,b,c):
    det = b**2 - (4*a*c)
    if det > 0:
            print("2 real root")
    elif det < 0:
        print("2 imaginary roots")
    else:
        print("1 real roots")
        
    sqrt_det = cmath.sqrt(det)
    root1 = (-b + sqrt_det)/(2*a)
    root2 = (-b - sqrt_det)/(2*a)
    print(f"The first root is {root1}")
    print(f"The second root is {root2}")

       
def main():
    
    print("Finding roots for equation (ax^2 + bx + c = 0)")
    a = int(input("Enter the value of 'a': "))
    b = int(input("Enter the value of 'b': "))
    c = int(input("Enter the value of 'c': "))

    roots(a,b,c)
    
main()


