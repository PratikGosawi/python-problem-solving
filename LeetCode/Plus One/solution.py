class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        carry_forward = 0

        if digits[i] < 9:
            digits[i] = digits[i] + 1
            return digits

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carry_forward = 1
            else:
                digits[i] = digits[i] + 1
                return digits
            
        
        digits.insert(0, carry_forward)
        return digits


        
        