class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        p=1
        temp = n
        while temp >0:
            d=temp%10
            s+=d
            p*=d
            temp=temp//10
        return (p-s)
    