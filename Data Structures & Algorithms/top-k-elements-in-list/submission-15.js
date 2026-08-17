class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const map = {};
        const freq = new Array(nums.length + 1).fill(0).map(() => []);
        const res = [];
        for (const i of nums){
            if(!map[i]){
                map[i] = 0;
            }
            map[i] = 1+map[i];
        }

        for (const [n,c] of Object.entries(map)){
            freq[c].push(n);
        }

        for (let i = freq.length-1; i >= 0; i--){
            for (const n of freq[i]){
                res.push(n);
                if(res.length == k){
                    return res;
                }
            }
        }

        return res;


        
    }
}
