class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        ans = 0
        dp = [0] * n

        for i in range(2, n):
            if nums[i-2] - nums[i-1] == nums[i-1] - nums[i]:
                dp[i] = dp[i-1] + 1
                ans += dp[i]

        return ans