'''

    Reverse the given sentence.
        Input: 'This is the best'
        Output: 'best the is This'

    Note: As part of this exercise you should remove all leading and trailing whitespace.

    1) Method1: use python built in functions split() & reversed()
    2) Method2: use python split() & a trick of printing left to right.
    3) Method3:

'''

class SentenceReversal:

    def __init__(self, s):
        self.s = s

    def method01(self):
        return " ".join(reversed(self.s.split()))

    def method02(self):
        return " ".join(self.s.split()[::-1])

    def rev_list(self, lst):
        rev_lst = []
        for word in lst[::-1]:
            rev_lst.append(word)
        return rev_lst

    def method03(self):
        words = []
        space = [' ']
        length = len(self.s)

        i = 0
        while i < length:
            if self.s[i] not in space:
                word_start = i
                while i < length and self.s[i] not in space:
                    i += 1
                words.append(self.s[word_start:i])
            i += 1
        return " ".join(self.rev_list(words))
        #return " ".join(list(reversed(words)))


obj1 = SentenceReversal('THE BEST k')
print obj1.method01()
print obj1.method02()
print obj1.method03()



