class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        Len = len(nums1)
        if Len % 2 == 0:
            return (nums1[int(Len / 2)] + nums1[int((Len / 2) - 1)]) /2
        else:
            return nums1[int((Len - 1) / 2)]