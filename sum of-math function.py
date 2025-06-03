def sumrange(xmin, xmax, xmultiplier, added): """ The components of the sum-of math function. Xmin is the
starting value, xmax is the maximum x value, xmultiplier is the value x is multiplied by, and added is
any value added to x. If there is no multiplier for x, type 1 for xmultiplier, and if there is no number
that is added to x, type 0 for added."""
    total = 0 #sets up the total variable.
    numberlist = list(range(xmin, (xmax+1))) #calculates the list of values for x.
    times_to_repeat = (xmax-xmin)+1 #calculates how many times to run the for loop.
    for x in range(times_to_repeat):
        number = numberlist[x] #gets each value of x.
        result = (number*xmultiplier)+added #calculates the result with the x value.
        total = total + result #collects the results.
    return total
