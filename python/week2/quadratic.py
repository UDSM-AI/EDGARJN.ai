import math as mt

def lap_quadratic(a,b,c):
    insider = (b**2 - (4*a*c))

    if insider > 0:
        x1 = (-b + mt.sqrt(insider))/(2*a)
        x2 = (-b-mt.sqrt(insider))/(2*a)

        print(f"\nSuccessfully calculated:\n x = {x1} or x = {x2}")

    else:
        print("\nI'm small mathematic model, it's complexity to me")


# ask data from a user
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

lap_quadratic(b=b, c=c, a=a)

