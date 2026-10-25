class Solution:
    def beautySum(self, s: str) -> int:
        # code here
        n = len(s)
        total = 0

        for i in range(n):
            freq = [0] * 26
            max_freq = 0

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                max_freq = max(max_freq, freq[idx])

                min_freq = n
                for count in freq:
                    if count > 0:
                        min_freq = min(min_freq, count)

                total += max_freq - min_freq

        return total
