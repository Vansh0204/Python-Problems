class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=0
        temp=x
        while temp>0:
            d=temp%10
            a=a*10+d
            temp=temp//10
        if(a==x):
            return True
        else:
            return False
        