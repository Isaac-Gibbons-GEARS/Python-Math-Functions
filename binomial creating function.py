from math import sqrt

def factor_list(number):
    positive_num = abs(number)
    factors = []
    factors_neg = []
    for i in range(positive_num):
        result = positive_num/(i+1)
        result_int = int(result)
        if result == result_int:
            factors.append(result)
    for x in factors:
        num = x*-1
        factors_neg.append(num)
    factors_total = factors + factors_neg
    return factors_total

def binomial(a,b,c):
    if a > 1:
        a = 1
        b = b/a
        c = c/a
    factors_of_c = factor_list(c)
    times_to_repeat = len(factors_of_c)
    num1 = 0
    num2 = 0
    operand1 = ""
    operand2 = ""
    for i in range(times_to_repeat):
        start = 0
        factor1 = factors_of_c[i]
        times_to_repeat2 = times_to_repeat-1
        for x in range(start,times_to_repeat2):
            start += 1
            factor2 = factors_of_c[x]
            product = factor1*factor2
            sumof = factor1+factor2
            if product == c and sumof == b:
                num1 = factor1
                num2 = factor2
                squareroot1 = sqrt((num1**2))
                squareroot2 = sqrt((num2**2))
                if squareroot1 == num1:
                    operand1 = "+"
                elif squareroot1 != num1:
                    operand1 = ""
                if squareroot2 == num2:
                    operand2 = "+"
                elif squareroot2 != num2:
                    operand2 = ""
    answer = f"(x{operand1}{num1})(x{operand2}{num2})"
    return answer
thing = binomial(1,-3,-10)
print(thing)