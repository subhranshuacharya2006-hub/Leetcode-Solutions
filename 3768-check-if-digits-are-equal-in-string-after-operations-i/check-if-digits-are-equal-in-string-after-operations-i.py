class Solution:
    def hasSameDigits(self, s):
        a = [int(x) for x in s]

        while len(a) > 2:
            b = []
            for i in range(len(a) - 1):
                b.append((a[i] + a[i + 1]) % 10)
            a = b

        return a[0] == a[1]