class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        
        let seen = new Map();

        for(let i = 0; i < nums.length; i++){
            let complimentary = target - nums[i];
            if (seen.has(complimentary)){
                return [seen.get(complimentary), i];
            }
            seen.set(nums[i], i);
        }


    }
}
