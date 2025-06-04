import math
try:
    name = "bla"
    name_number = float(name)
    print(name_number)
    print(type(name_number))
except ValueError:
    print("can't turn string to float.")
    
def hypotenuse(first, second):
    long_side = math.sqrt(first**2+second**2)
    return long_side
long = hypotenuse(3, 4)
print(long)

def hypotenuseFunction2(first2, second2):
    long_side2 = 