#ways of solving this problem
# 1) if both strings having the same characters & same frequency.
# 2) sort both strings and compare them together. if they are identical then one is anagram of other.

class AnagramCheck:

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    # remove spaces or spaces not counted AND not case sensitive
    def apply_conditions(self, str):
        return str.replace(' ','').lower()

    def anagram_method_01(self):

        # check if length of both strings
        s1 = self.apply_conditions(self.s1)
        s2 = self.apply_conditions(self.s2)

        #Edge case check
        if len(s1) != len(s2):
            return False

        #using dictionaries to keep track of characters by key value pairs
        count = {}
        for letter in s1:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

        for letter in s2:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1

        for k in count:
            if count[k] != 0:
                return False

        return True

    def anagram_method_02(self):
        s1 = self.apply_conditions(self.s1)
        s2 = self.apply_conditions(self.s2)
        return sorted(s1) == sorted(s2)

obj1 = AnagramCheck('GOD', 'dog')
print 'method 1: ', obj1.anagram_method_02()
print 'method 2: ', obj1.anagram_method_01()