#Problem 66 - Easy

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        add = 0
        for i in range(length-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                add = 1
            else:
                digits[i] = digits[i] + 1
                add = 0
                break
        if add == 1:
            digits.insert(0, 1)
        return digits

        