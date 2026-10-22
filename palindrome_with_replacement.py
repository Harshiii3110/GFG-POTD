class Solution:
    def minimumSum(self, s: str) -> int:
        # code here
        n = len(s)
        half = []

        for i in range(n // 2):
            j = n - 1 - i

            if s[i] != '?' and s[j] != '?' and s[i] != s[j]:
                return -1

            if s[i] != '?':
                half.append(s[i])
            elif s[j] != '?':
                half.append(s[j])
            else:
                half.append('?')

        total = 0
        previous = None

        for ch in half:
            if ch == '?':
                continue

            if previous is not None:
                total += abs(ord(ch) - ord(previous))

            previous = ch

        return 2 * total
