class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        m = 8 * n * n

        # Generate the original first coil
        coil1 = [0] * m

        coil1[0] = 8 * n * n + 2 * n
        curr = coil1[0]

        flag = 1
        step = 2
        index = 1

        while index < m:

            # Move vertically
            for _ in range(step):
                curr = curr - 4 * n * flag
                coil1[index] = curr
                index += 1

                if index >= m:
                    break

            if index >= m:
                break

            # Move horizontally
            for _ in range(step):
                curr = curr + flag
                coil1[index] = curr
                index += 1

                if index >= m:
                    break

            flag *= -1
            step += 2

        # The second coil is obtained using the complementary value
        total = 16 * n * n + 1
        coil2 = [total - x for x in coil1]

        # GFG judge's required orientation
        return [coil2[::-1], coil1[::-1]]
