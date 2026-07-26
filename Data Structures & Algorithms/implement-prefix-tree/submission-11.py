class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = PrefixTree()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return True
        