class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            if target == nums[mid]: 
                return mid

            # If the left half is sorted
            if nums[l] <= nums[mid]:
                # If target is greater than mid OR smaller than our left bound, search right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # If the right half is sorted
            else:
                # If target is smaller than mid OR greater than our right bound, search left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
