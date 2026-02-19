class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):

            # If digit is less than 9 → just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9 → make it 0 and continue carry
            digits[i] = 0

        # If loop finishes → all digits were 9
        return [1] + digits
