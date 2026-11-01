class Solution:

    def maximumSubarray(self, arr: list[int]) -> int:
        """ code here """
        no_square = arr[0]
        one_square = arr[0] * arr[0]

        ans = max(no_square, one_square)

        for i in range(1, len(arr)):
            x = arr[i]

            new_one_square = max(
                no_square + x * x,
                one_square + x,
                x * x
            )

            new_no_square = max(
                no_square + x,
                x
            )

            no_square = new_no_square
            one_square = new_one_square

            ans = max(ans, no_square, one_square)

        return ans
