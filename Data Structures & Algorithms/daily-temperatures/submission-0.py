class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        enum = list(enumerate(temperatures))

        stack = []

        for e in enum:
            while stack and stack[-1][1] < e[1]:
                thing = stack.pop()  # what to do with popped things?
                result[thing[0]] = e[0] - thing[0]
            stack.append(e)

        return result
