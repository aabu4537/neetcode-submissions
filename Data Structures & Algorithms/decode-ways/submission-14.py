class Solution:
    def numDecodings(self, s: str) -> int:
        # Guard clause: a string starting with '0' cannot be decoded
        if not s or s[0] == "0":
            return 0

        # prev represents dp[i-2], cur represents dp[i-1]
        # Initially, for length 0 and length 1, both have 1 valid way
        prev, cur = 1, 1

        # Walk through the string starting from the second character
        for i in range(1, len(s)):
            # We will build the 'next_dp' value for the current position
            next_dp = 0

            # 1. Single-digit check: Can s[i] stand alone? (Not '0')
            if s[i] != "0":
                next_dp += cur

            # 2. Two-digit check: Is s[i-1:i+1] a valid letter (10-26)?
            two_digit = int(s[i-1 : i+1])
            if 10 <= two_digit <= 26:
                next_dp += prev

            # Shift our variables forward for the next iteration
            prev = cur
            cur = next_dp

        return cur
