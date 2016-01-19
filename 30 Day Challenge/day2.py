'''
Arithmetic!
'''
m = float(input())
t = int(input())
x = int(input())

tip = (t*m) / 100 
tax = (x*m) / 100
price = round(m + tip + tax)
print("The final price of the meal is ${}.".format(int(price)))