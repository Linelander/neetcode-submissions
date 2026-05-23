class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.ending = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = PrefixTree()
            curr = curr.children[i]
        curr.ending = True

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]
            ind = ord(c) - ord('a')
            if not curr.children[ind]:
                return False
            curr = curr.children[ind]
        return curr.ending


    def startsWith(self, prefix: str) -> bool:
        curr = self

        for i in range(len(prefix)):
            c = prefix[i]
            ind = ord(c) - ord('a')
            if not curr.children[ind]:
                return False
            curr = curr.children[ind]

        
        return True
        