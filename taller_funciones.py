def computepay(h,r):
    if h <= 40 :
        return  print("pay",h*r)
    elif h > 40 :
        pay = 0
        pay = 40 * r
        pay = pay + (h - 40) * r * 1.5
        return print ("Pay",pay)

hrs = float(input("Enter Hours:\n"))
rate = float(input("Enter Rate:\n"))

try:
    x1 = float(hrs)
    x2 = float(rate)
except:
    print("Error, please enter numeric imput")
    quit()
computepay(x1,x2)

