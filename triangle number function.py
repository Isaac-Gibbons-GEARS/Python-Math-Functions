def trinumber(value):
    total = 0 #sets up the total variable
    numberlist = list(range(1,(value+1))) #creates the list of numbers to be added
    times_to_repeat = len(numberlist) #finds the number of times the for loop needs to repeat
    for i in range(times_to_repeat):
        number = numberlist[i] #gets the numbers to be added
        total = total + number #adds the numbers to each other and stores them in total
    return total
thing = trinumber(5)
print(thing)
        