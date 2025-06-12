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

loop = True
while loop:
    number_input = input("Enter the number to be factored: ")
    Factors_of_number = factor_list(number_input)
    print(Factors_of_number)
    print("Would you like to restart? (yes/no)")
    loop_response = input().lower()
    if loop_response == "yes":
        continue
    else:
        loop = False
