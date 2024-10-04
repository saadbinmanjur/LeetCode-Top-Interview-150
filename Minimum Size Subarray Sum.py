class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        w_sum = 0
        start = 0

        for i in range(n):
            w_sum += nums[i]

            while w_sum >= target:
                ans = min(ans, i - start + 1)
                w_sum -= nums[start]
                start += 1

        return 0 if ans == float('inf') else ans