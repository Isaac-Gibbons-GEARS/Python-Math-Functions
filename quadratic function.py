def quadratic(a,b,c,):
    from math import sqrt
    x1 = ((-1*b)+sqrt(((b**2)-(4*a*c))))/(2*a)
    x2 = ((-1*b)-((b**2)-(4*a*c)))/(2*a)
    answers = f"{x1} and {x2}"
    return answers
thing = quadratic(1,3,2)
print(thing)