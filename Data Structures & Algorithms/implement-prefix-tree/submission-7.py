class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.refs = 0
        self.ending = False

    def insert(self, word: str) -> None:
        curr = self
        curr.refs += 1

        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = PrefixTree()
            curr = curr.children[i]
            curr.refs += 1

        curr.ending = True

    def search(self, word: str) -> bool:
        curr = self

        for i in range(len(word)):
            c = word[i]
            ind = ord(c) - ord('a')
            if not curr or curr.refs == 0:
                return False
            if not curr.children[ind]:
                return False
            curr = curr.children[ind]

        if not curr: return False
        
        return curr.ending


    def startsWith(self, prefix: str) -> bool:
        curr = self

        for i in range(len(prefix)):
            c = prefix[i]
            ind = ord(c) - ord('a')
            if not curr or curr.refs == 0:
                return False
            if not curr.children[ind]:
                return False
            curr = curr.children[ind]

        
        return True
        