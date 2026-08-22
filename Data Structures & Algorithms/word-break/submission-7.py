class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #brute force check if any possible substring exists in the wordDict probably be O(n^2) time
        #thinking sliding window

        word_set = set(wordDict)
        dp = [False] * (len(s) +1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

        