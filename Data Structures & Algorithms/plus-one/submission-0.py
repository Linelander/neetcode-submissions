class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for x in range(len(digits)-1, -1, -1):
            if digits[x] < 9:
                digits[x] = digits[x] + 1
                break
            else:
                digits[x] = 0
                if x == 0:
                    digits = [1] + digits
            x -= 1

        return digits