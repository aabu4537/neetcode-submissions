class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) -1
        min_n = float('inf')
        while l < r:
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid

        return nums[l]
        