hrs = input("Enter Hours: ")
tr = input("Enter Tarifa: ")
pay = 0

try:
    x1 = float(hrs)
    x2 = float(tr)
except:
    print("Error, please enter numeric input")
    quit()
if x1 <= 40 :
    pay = x1 * x2
    print(pay)
elif hrs > 40:
    pay = 40 * x2
    pay = pay + (x1 - 40) * x2 *1.5
    print(pay)

    