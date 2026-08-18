class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {

        const res = [];

        nums.sort((a, b) => a-b);

        for (let i = 0; i < nums.length; i++){
            let a = nums[i];
            if (i>0 && a == nums[i-1]){
                continue;
            }
            let l = i+1;
            let r = nums.length -1;
            while (l < r){
                let three = a + nums[l] + nums[r];
                if(three > 0){
                    r--;
                } else if (three < 0) {
                    l++;
                } else {
                    res.push([a, nums[l], nums[r]])
                    l++;
                    while (l<r && nums[l-1] == nums[l]){
                        l++;
                    }
                }



            }
        }

        return res;

    }
}
