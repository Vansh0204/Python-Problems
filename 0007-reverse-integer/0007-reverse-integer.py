class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0

        while x != 0:
            digit = x % 10
            x //= 10

            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0

            res = res * 10 + digit

        res *= sign

        if res < INT_MIN or res > INT_MAX:
            return 0

        return res