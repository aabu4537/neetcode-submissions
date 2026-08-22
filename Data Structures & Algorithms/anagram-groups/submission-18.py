class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:
            alphabet = [0] *26
            for l in word:
                alphabet[ord(l) - ord('a')] +=1
            groups[tuple(alphabet)].append(word)
        
        return list(groups.values())

        
        