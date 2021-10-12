def computepay():
    pay = (hours * rate)
    print(pay)

try:
    hours = float(input("Enter hours per week here: "))
    rate = float(input("Enter your rate here: "))

    if hours > 40:
        overpay = (hours - 40) * 1.5 * rate
        total = overpay + (40 * rate)
        print (f"Your pay seems to be: {total}")
    else:
        computepay()
except:
    print("Error,please use numeric input")
