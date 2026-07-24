class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # take in list of strings
        # return list of grouped string if they are anagrams
        # will integrate anagram logic of array of alpahbet
        # will have hashmap {key = array of alphabet: value: list of strings}

        hashmap = defaultdict(list)

        for word in strs:
            alphabet = [0] * 26
            for letter in word:
                alphabet[ord(letter) - ord('a')] += 1
            hashmap[tuple(alphabet)].append(word)
        
        return list(hashmap.values())
        