def sum_cumulative(l):
    for i in range(1, len(l)):
        l[i] = l[i] + l[i-1]
    return(l)

print(sum_cumulative([1,2,3,4,5,6]))