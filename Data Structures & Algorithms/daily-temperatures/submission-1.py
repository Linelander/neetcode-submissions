class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use append and pop for stacks
        
        result = [0] * len(temperatures)
        stack = []
        stack.append([temperatures[0], 0])

        for i in range(1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                j = stack[-1][1]
                result[j] = i - j
                stack.pop()
            stack.append([temperatures[i], i])

        return result