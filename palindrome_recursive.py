'''A palindrome is a word, phrase, or sequence that reads the same backward as forwards. Use recursion to check if a given string is palindrome or not.
Input
User Task:
Since this is a functional problem, you don't have to worry about the input. You just have to complete the function is_palindrome(s), where you will get the input string as the argument.


Constraints:

1 ≤ T ≤ 100
1 ≤  N ≤ 10000

Output
Return true if given string is palindrome else return false

Example
Sample Input
2
ab
aba

Sample Output
false
true'''

def is_palindrome(s):
    if s=="":
        return True
    else:
        if s[0]==s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
