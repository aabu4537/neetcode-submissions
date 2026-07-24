class Solution:
    def isPalindrome(self, s: str) -> bool:

        checker = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                checker += char.lower()
        print(checker)
        return checker == checker[::-1]

        