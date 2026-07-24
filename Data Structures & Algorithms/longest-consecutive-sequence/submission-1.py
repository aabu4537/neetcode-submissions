class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #brute force is to sort it , then take note of highest counter sort algos can be anywhere from O(n) to O(nlogn) time
        #O(n) time complexity we need to use a hashset?
        # can make nums into hashset and if num in hash set increment counter and take note of highest counter as we iterate once through the list

        sett = set(nums)
        max_count = 0
        for num in nums:
            if num-1 not in sett:
                curr = num
                counter = 0
                while curr in sett:
                    counter+=1
                    curr +=1
                max_count = max(max_count, counter)
        return max_count




            