class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        # code here
        vowels = set('aeiou')
        n = len(s)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i]

            if s[i] in vowels:
                prefix[i + 1] += 1

        result = []

        for l, r in queries:
            count = prefix[r + 1] - prefix[l]
            result.append(count)

        return result
