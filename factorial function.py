def factorial(value):
    total = 1 """this is different from the others because it's multiplication, not addition. If it was 0 total would
              would always equal 0, because the first value in the list would be multiplied by 0, which would equal 0,
              then the next would be multiplied by that, and so on."""
    numberlist = list(range(1,(value+1))) #creates the list of numbers to be multiplied.
    times_to_repeat = len(numberlist) #finds the number of times the for loop needs to repeat.
    for i in range(times_to_repeat):
        number = numberlist[i] #gets the number to be multiplied
        total = total * number # multiplies the number and stores it in total
    return total
thing = factorial(10)
print(thing)
        
