def sumrangesqr(xmin, xmax, base, added):
    """ The components of the sum-of math function, but specifically tailored for sum of functions when x is an exponent. Example: 2^x + 3. Xmin is the
    starting value, xmax is the maximum x value, base is the number x raises,
    and added is any value added to x. In the previous example, 2 = the base and 3 equals added. Unfortunately python doesn't allow
    sum of figures, so that, the best example I can give in the code. If there is no multiplier for x, type 1 for base,
    and if there is no number that is added to x, type 0 for added."""   
    total = 0  # Set up the total variable
    numberlist = list(range(xmin, xmax + 1))  # Calculates the list of values for x
    times_to_repeat = (xmax-xmin)+1 #calculates how many times to run the for loop.
    for x in range(times_to_repeat):
        number = numberlist[x] #gets each value of x.
        result = (base**number)+added #calculates the result with the x value.
        total = total + result #collects the results.
    return total
