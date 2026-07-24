class Node:
    def __init__(self):
        self.last = False
        self.children = {}

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root

        for l in word:
            if l not in cur.children:
                cur.children[l] = Node()
            cur = cur.children[l]
        
        cur.last = True


    def search(self, word: str) -> bool:
        cur = self.root

        for l in word:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        return cur.last
        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root

        for l in prefix:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        
        return True
        
        