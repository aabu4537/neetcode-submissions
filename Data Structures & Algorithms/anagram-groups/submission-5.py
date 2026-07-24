class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #anagrams array of 26 reps each letter in alphabet
        # {alphabet array: actual word} 
        # time complexity of O(m * n) space complexity of O(m)
        #

        dictionary = defaultdict(list)

        for word in strs:
            alphabet = [0] * 26
            for letter in word:
                alphabet[ord(letter) - ord('a')] += 1
            dictionary[tuple(alphabet)].append(word)

        return list(dictionary.values())        

