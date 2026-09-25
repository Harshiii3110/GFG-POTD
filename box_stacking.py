class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        # Code here
        n = len(height)
        boxes = []
        for i in range(n):
            a = height[i]
            b = width[i]
            c = length[i]
            boxes.append((max(b, c), min(b, c), a))
            boxes.append((max(a, c), min(a, c), b))
            boxes.append((max(a, b), min(a, b), c))
        memo = {}
        def solve(base1, base2):
            key = (base1, base2)
            if key in memo:
                return memo[key]
            best = 0
            for b1, b2, h in boxes:
                if b1 < base1 and b2 < base2:
                    best = max(best, h + solve(b1, b2))
            memo[key] = best
            return best
        answer = 0
        for b1, b2, h in boxes:
            answer = max(answer, h + solve(b1, b2))
        return answer
