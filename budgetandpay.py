#Make a new program to compute someone's pay for a week, a month, a year
#Be sure to include tax rate as well
#This will not include medical insurance deductions from the pay
print("This program calculates pay for time worked and monthly expenses. Overtime is considered anything over 40 hours")
print()
inp = input("Name: ")
try:
    inp = input("Enter hours worked: ")
    hours = float(inp)
    inp = input("Enter rate/hour: $")
    rate = float(inp)
    inp = input("tax(%): ")
    tax = float(inp)/100
except:
    print("Error! Please enter numeric values")
    
if hours > 40:
    grosspay = rate * 40 + (1.5 * rate * (hours - 40))
else:
    grosspay = rate * hours

netpay_week = grosspay - (tax * grosspay)
print()
print("grosspay for the week is $", grosspay)
print("netpay for the week is $", netpay_week)

netpay_month = netpay_week * 4
print("netpay for the month is $", netpay_month)

netpay_year = netpay_month * 12
print("netpay for the year is $", netpay_year)
print()
print()
print()

x = 5
while x == 5:
    inp1 = input('Enter expense name(if there are no more expenses type "none" and press Enter: ')
    if inp1 == 'none':
        print("End of monthly expenses")
        break
    else:
        inp = input("Enter minimum monthly payment: $")
        expmonth = float(inp)
        print()
        expyear = expmonth * 12
        print("Total yearly expense of ", inp1, " is $", expyear)
        print()
        print("Total monthly expense of ", inp1, " is $", expmonth)
        print()
        print()
        print()
        print()
        












