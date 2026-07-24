class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k < 2:
            return nums
        
        n = len(nums)
        res = []
        l,r = 0, k
        while r <= n:
            temp = 0
            for i in range(l, r):
                temp = max(nums[i], temp)
            res.append(temp)
            l+=1
            r+=1
        return res


        

            