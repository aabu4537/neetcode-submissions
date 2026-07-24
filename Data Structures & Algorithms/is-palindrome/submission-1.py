class Solution:
    def isPalindrome(self, s: str) -> bool:

        empty = []

        for char in s:
            if char.isalnum():
                empty.append(char.lower())

        return empty == empty[::-1]            
        