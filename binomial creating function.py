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

def tobinomial(a,b,c,var_symbol="x"):
    if a == 1:       
        factors_of_c = factor_list(c)
        times_to_repeat = len(factors_of_c)
        num1 = 0
        num2 = 0
        operand1 = ""
        operand2 = ""
        for i in range(times_to_repeat):
            factor1 = factors_of_c[i]
            for x in range(0,times_to_repeat):
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
    elif a != 1:
        new_c = a*c
        factors_of_c = factor_list(new_c)
        times_to_repeat = len(factors_of_c)
        num1 = 0
        num2 = 0
        operand1 = ""
        operand2 = ""
        for i in range(times_to_repeat):
            factor1 = factors_of_c[i]
            for x in range(0,times_to_repeat):
                factor2 = factors_of_c[x]
                product = factor1*factor2
                sumof = factor1+factor2
                if product == new_c and sumof == b:
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
    if num1 and num2 == 0:
        answer = "no solution by this method"
    else:
        answer = f"({var_symbol}{operand1}{num1})({var_symbol}{operand2}{num2})"
    return answer
thing = tobinomial(2,7,3)
print(thing)
