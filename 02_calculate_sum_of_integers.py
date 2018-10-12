
import cProfile
import timeit

def sum1(n):
    final_sum =0

    for x in range(n+1):
        final_sum += x
    return final_sum

#best approach by considering time complexity
def sum2(n):
    return (n*(n+1)/2)


value1= sum1(10)
value2= sum2(10)

print timeit.timeit("sum1(100000000)", "from __main__ import sum1", number=1)
print timeit.timeit("sum2(100000000)", "from __main__ import sum2", number=1)