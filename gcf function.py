def gcf(*args):
    numbers = list(args)
    numbers.sort()
    factors = []
    for number in numbers:
        for i in range(1,number):
            result = number%i
            if result == 0 and i not in factors:
                factors.append(i)
    for x in numbers:
        for y in factors:
            quotient1 = x/y
            if int(quotient1) != float(quotient1):
                if factors.index(y) == (len(factors)-2):
                    last = factors[(len(factors)-1)]
                    quotient2 = x/last
                    if int(quotient2) != float(quotient2):
                        factors.remove(last)
                factors.remove(y)
                    
    factors.sort(reverse=True)
    return factors[0]
print(gcf("put your numbers here seperated by commas"))