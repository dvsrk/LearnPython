
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

print timeit.repeat("for x in range(10): sum1(x)", "from __main__ import sum1", number=10)
print timeit.repeat("for x in range(10): sum2(x)", "from __main__ import sum2", number=10)