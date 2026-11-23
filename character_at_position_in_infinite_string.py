class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        # code here
        lengths = [len(s)]

        step = 1

        while lengths[-1] < pos:
            new_length = 2 * lengths[-1] + step
            lengths.append(new_length)
            step += 1

        for i in range(len(lengths) - 1, 0, -1):
            old_length = lengths[i - 1]

            if pos <= old_length:
                continue

            elif pos <= old_length + i:
                return '$'

            else:
                pos = 2 * old_length + i - pos + 1

        return s[pos - 1]
