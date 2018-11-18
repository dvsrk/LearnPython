'''
Given an integer array, output all the unique pairs that sum up to a specific value k.
Input: pair_sum([1,3,2,2],4)
Output:
 (1,3)
 (2,2)
'''

class ArrayPairSum:

    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def method(self):

        'Edge case check
        if len(self.arr) < 2:
            return

        #Sets for trackin
        seen = set()
        output = set()

        for num in self.arr:
            diff = self.target - num
            if diff not in seen:
                seen.add(num)
            else:
                output.add((min(diff,num),max(diff, num)))
        print output
        print seen
        print '\n'.join(map(str,list(output)))

obj1 = ArrayPairSum([1,3,2,2,5,-1],4)
obj1.method()