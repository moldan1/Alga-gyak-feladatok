class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp_minusz_two = 1
        dp_minusz_one = 2
        for _ in range(3, n + 1):
            current_dp = dp_minusz_one + dp_minusz_two
            dp_minusz_two = dp_minusz_one
            dp_minusz_one = current_dp
        return dp_minusz_one