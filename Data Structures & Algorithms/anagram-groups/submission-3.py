class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #hashmap (alphabet counter : list of words)

        hashmap = defaultdict(list)


        for word in strs:
            alphabet = [0] * 26
            for letter in word:
                alphabet[ord(letter) - ord('a')] += 1# a = 80 b=81 =[1]
            hashmap[tuple(alphabet)].append(word)
        
        return list(hashmap.values())