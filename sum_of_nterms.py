#sum of nterms
# 1 - 3x^3/3! + 5x^5/5! - 7x^7/7! ...... nterms

def main():
    n  = int(input("Enter the number of terms: "))
    x = float(input("Enter the value of x: "))
    sum_s = 1
    sign = 1
    coe = 1
    fact = 1
    x_val = x
    
    for i in range(2,n+1):
        sign = sign *(-1)
        coe = coe + 2
        fact = fact * (coe-1) * coe
        x_val =  x_val* (x**2)
        term = (sign * coe * x_val)/fact
        sum_s = sum_s + term

    print(f'The sum of {n} terms is {sum_s}')

main()
