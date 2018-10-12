
import cProfile

def sum1(n):
    final_sum =0

    for x in range(n+1):
        final_sum += x
    return final_sum

#best approach by considering time complexity
def sum2(n):
    return (n*(n+1)/2)


print sum1(10)
print sum2(10)
