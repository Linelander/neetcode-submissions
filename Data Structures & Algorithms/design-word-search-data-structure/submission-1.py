class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = WordDictionary()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        
        for i in range(len(word)):
            c = word[i]
            ind = ord(c) - ord('a')
            
            if c == '.': # recur to all children
                recurres = False
                for child in curr.children:
                    if child: recurres |= child.search(word[i+1:]) # result should be true if any one of them is positive
                return recurres
            elif not curr.children[ind]:
                return False
            curr = curr.children[ind]
            
        if not curr or not curr.end:
            return False
        return True
