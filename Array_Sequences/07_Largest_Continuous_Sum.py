'''
    Given an array of integers (positive and negative) find the largest continuous sum.
    If the array is all positive, then the result is simply the sum of all numbers.
    The negative numbers in the array will cause us to need to begin checking sequences.
    The algorithm is, we start summing up the numbers and store in a current sum variable.
    After adding each element, we check whether the current sum is larger than maximum sum encountered so far.
    If it is, we update the maximum sum. As long as the current sum is positive, we keep adding the numbers.
    When the current sum becomes negative, we start with a new current sum.
    Because a negative current sum will only decrease the sum of a future sequence.
    Note that we dont reset the current sum to 0 because the array can contain all negative integers.
    Then the result would be the largest negative number.
'''

class LargestContinuousSum:

    def __init__(self, arr):
        self.arr = arr

    def method01(self):

        #Edge case check
        if len(self.arr) == 0:
            return 'none'

        #Find if there are any negative numbers, if not return just the sum of all list elements.
        sum = 0
        negative = 0
        for num in self.arr:
            if num < 0:
                negative = 1
                break
            else:
                sum += num
        if negative == 0:
            return sum

        #Find largest continuous sum
        long_sum = current_max = self.arr[0]
        for num in self.arr[1:]:
            current_max = max(current_max+num,num)
            long_sum = max(current_max,long_sum)
        return long_sum

obj1 = LargestContinuousSum([1, 2, 1, 10])
print obj1.method01()


