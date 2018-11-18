'''
    Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array
    and deleting a random element. Given these two arrays, find which element is missing in the second array.
    Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
    Input:
        finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
    Output:
        5 is the missing number

    Options:
        1) Brute force approach where each element from the second array is compared with every element on first array.
            O(N2) --> Since it need two FOR loops to do that
        2) The most efficient solution is to sort the first array, while checking whether an element in the first array
            appears in the second array.
            O(NlogN)
        3) Calculate sum of array1 & sum of array2 then subtract each other. The difference is the missing number.
        4) Sort both arrays and iterate over them simultaneously. Once two arrays have different arrays we can stop.
            O(NlogN)
'''

class FindMissingElement:

    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def method1(self):
        arr1 = sorted(self.arr1)
        arr2 = sorted(self.arr2)
        for num1, num2 in zip(arr1,arr2):
            if num1 != num2:
                return num1
        return 'none'

    def method2(self):
        count = {}
        for num in self.arr1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num in self.arr2:
            if num in count:
                count[num] -= 1

        for x in count:
            if count[x] != 0:
                return x
        return 'none'

    def method3(self):
        sum1 = sum(self.arr1)
        sum2 = sum(self.arr2)
        diff = sum1 - sum2
        if diff != 0:
            return diff

obj1 = FindMissingElement([1,2,3,4,5,6,7],[3,2,1,5,6,7])
print obj1.method1()
print obj1.method2()
print obj1.method3()