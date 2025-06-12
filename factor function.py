def factor_list(number):
    factors = []
    factors_neg = []
    for i in range(number):
        result = number/(i+1)
        result_int = int(result)
        if result == result_int:
            factors.append(result)
    for x in factors:
        num = x*-1
        factors_neg.append(num)
    factors_total = factors + factors_neg
    return factors_total
thing = factor_list(24)
print(thing)
    