class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for i in nums:
            if end < 0:
                return False
            elif i > end:
                end = i
            end -= 1
        return True