class Node:

    def __init__(self):
        self.last = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for l in word:
            if l not in cur.children:
                cur.children[l] = Node()
            cur = cur.children[l]

        cur.last = True

    def search(self, word: str) -> bool:

        def helper(node, i):
            cur = node

            for j in range(i, len(word)):
                
                if word[j] == ".":
                    for c in cur.children.values():
                        if helper(c, j+1): return True
                    return False
                else:
                    if word[j] not in cur.children:
                        return False
                    cur = cur.children[word[j]]

            return cur.last

        return helper(self.root, 0)
        
