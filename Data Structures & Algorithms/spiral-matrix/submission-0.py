class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [0, 1] # y, x

        seenall = len(matrix) * len(matrix[0])
        numseen = 0

        seen = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        result = []


        curr = [0, 0]
        while numseen < seenall:
            result.append(matrix[curr[0]][curr[1]])
            seen[curr[0]][curr[1]] = 1
            numseen += 1
            
            nr, nc = curr[0] + direction[0], curr[1] + direction[1]
            if (nr < 0 or nr >= len(matrix)
                or nc < 0 or nc >= len(matrix[0])
                or seen[nr][nc] == 1):
                direction = [direction[1], -direction[0]]

            # apply direction
            curr = tuple(a + b for a, b in zip(curr, direction))

        return result