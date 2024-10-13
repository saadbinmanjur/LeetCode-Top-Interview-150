class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_set = {}

        for idx in range(len(nums)):
            if nums[idx] in h_set and abs(idx - h_set[nums[idx]]) <= k:
                return True
            h_set[nums[idx]] = idx
        return False