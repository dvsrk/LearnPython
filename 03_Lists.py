import timeit

num = 10000

def method1():
    l = []
    for n in xrange(num):
        l = l + [n]
    print l[0]

def method2():
    l = []
    for n in xrange(num):
        l.append(n)
    print l[0]

def method3():
    l = [n for n in xrange(num)]
    print l[0]

def method4():
    l = range(num)
    print l[0]

#method1()
#method2()
#method3()
#method4()
print timeit.timeit("method1()", "from __main__ import method1, num", number=1)
print timeit.timeit("method2()", "from __main__ import method2, num", number=1)
print timeit.timeit("method3()", "from __main__ import method3, num", number=1)
print timeit.timeit("method4()", "from __main__ import method4, num", number=1)