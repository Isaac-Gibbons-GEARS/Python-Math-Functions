def lcm(*args):
    multiples = []
    multiplier = 0
    count = 0
    com_mults = []
    total_counts = []
    while count != len(args):
        for i in args:
            multiple = i*(multiplier+1)
            multiples.append(multiple)
        for y in multiples:
            counts = multiples.count(y)
            total_counts.append(counts)
            if len(args) in total_counts:
                count = len(args)
                com_mults.append(y)
                break
        multiplier += 1
    com_mults.sort()
    return com_mults[0]
thing = lcm(9,5,18)
print(thing)
        