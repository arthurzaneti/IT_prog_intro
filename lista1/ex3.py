def nested_sum(l):
    total = 0
    for z in l:
        total += sum(z)
    return(total)

print(nested_sum([[1,2], [3,4]]))

