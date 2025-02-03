'''Given an integer x, return true if x is a palindrome, and false otherwise.'''
def isPalindrome(x):
    d=0
    temp=x
    while temp>0:
        a=temp%10
        d=d*10+a
        temp=temp//10
    if d==x:
        return bool(1)
    else:
        return bool(0)
