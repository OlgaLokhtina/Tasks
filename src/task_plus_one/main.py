class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            if len(digits) == 1:
                digits[-1] = 0
                digits.insert(0, 1)
                return digits
            else:
                rezult = self.plusOne(digits[:-1]) + [0]
                return rezult
