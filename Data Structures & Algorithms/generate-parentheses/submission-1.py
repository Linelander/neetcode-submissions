class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = []

        def recur(curr, op, clos):
            if len(curr) >= n*2:
                result.append(''.join(curr))
                return
            
            if op < n:
                curr.append('(')
                recur(curr, op + 1, clos)
                curr.pop()
            if clos < op:
                curr.append(')')
                recur(curr, op, clos + 1)
                curr.pop()

        recur(['('], 1, 0)
        return result

