#payroll calculator

def main():  
    basic = int(input("Enter your basic pay: "))
    tax = int(input("Enter tax amount: "))
    insurance = int(input("Enter your insurance: "))
    loan = int(input("Enter loan amount: "))
    
    gross = gross_sal(basic)
    print(f'gross = {gross}')
    deduct = deduction(tax, insurance, loan)
    print(f'deduction = {deduct}')
    net = net_sal(gross, deduct)
    print(f'The net salary is {net}')

def gross_sal(basic):
    if basic < 50000:
        hra = basic * 0.35
        da = basic * 0.1
        ca = basic * 0.15
    else:
        hra = basic * 0.25
        da = basic * 0.05
        ca = basic * 0.1
    return( basic + hra + ca + da)

def deduction(tax, insurance, loan):
    return(tax + insurance + loan)

def net_sal(gross, deduct): 
    return(gross - deduct)

main()
