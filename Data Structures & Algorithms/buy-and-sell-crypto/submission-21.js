class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {

        let max_profit = 0;
        let min_val = Number(Infinity);

        for (const p of prices){
            if(min_val > p){
                min_val = p;
            }
            max_profit = Math.max(max_profit, p - min_val);
        }


        return max_profit;

    }
}
