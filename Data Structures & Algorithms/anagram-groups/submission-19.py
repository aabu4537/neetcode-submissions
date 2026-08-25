class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for w in strs:
            alphabet = [0] * 26
            for l in w:
                alphabet[ord(l) - ord('a')] +=1
            res[tuple(alphabet)].append(w)

        return list(res.values())    