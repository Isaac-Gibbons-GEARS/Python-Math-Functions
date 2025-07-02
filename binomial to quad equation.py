def frombinomial(a,b): #this takes in the numbers in the binomial pair
    B = a+b #creates what would be b in a quadratic equation
    C = a*b #creates what would be c in a quadratic equation
    symbolB = "" 
    symbolC = ""
    absB = abs(B) #creates a positive version of b
    absC = abs(C) #creates a positive version of c
    if absB == B: #checks if b needs a symbol in front of it
        symbolB = "+"
    if absC == C: # checks if c needs a symbol in front of it
        symbolC = "+"
    quad_equation = f"x^2{symbolB}{B}x{symbolC}{C}"
    print(quad_equation)
