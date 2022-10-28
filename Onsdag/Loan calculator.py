Loan = 0
Interest = 0
Duration = 0
Monthly_payment = 0
Number_of_payments = 0

def percent(a, b):
    return (a / b) * 100
float(percent(25, 750))

strLoan = input("How much do you want to borrow? ")
strpercent = ("Helloouu")
strDuration = input("How many years will it take to pay back? ")


Duration = float(strDuration)
Loan = float(strLoan)
Interest = (percent)

Number_of_payments = Duration*12

Monthly_payment = Loan * Interest * (1+ Interest) * Number_of_payments \
    / ((1 + Interest) * Number_of_payments -1)

#print("Your monthly payment will be " + str(Monthly_payment))

print("Your monthly payment will be $%.2f" %Monthly_payment)