import math
print("Enter the coefficients of a, b and c: ", end = "")
a,b,c = map(int, input().split())

d = (b ** 2) - (4 * a * c)

if d < 0:
  x1 = (-b + math.sqrt(abs(d)))) / (2*a)
  x2 = (-b - math.sqrt(abs(d)))) / (2*a)
  print("The roots are imaginary:", "{0:.2f}".format(x1), end = "i and ")
  print("{0:.2f}".format(x2), end="i\n")
    
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print("This equation has one solution: ", x)

elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("This equation has two real solutions: ", "{0:.2f}".format(x1), " and", "{0:.2f}".format(x2))
