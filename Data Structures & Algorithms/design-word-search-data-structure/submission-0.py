class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.ending = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            ci = ord(c) - ord('a')
            if not curr.children[ci]:
                curr.children[ci] = WordDictionary()
            curr = curr.children[ci]
        curr.ending = True
            
    def search(self, word: str) -> bool:
        curr = self
        
        for i in range(len(word)):
            c = word[i]
            ci = ord(c) - ord('a')

            if c == '.': # need to recur... to all children?
                recurres = False
                for child in curr.children:
                    if child: recurres = recurres or child.search(word[i+1:]) #.......
                return recurres
            elif not curr.children[ci]:
                return False
            curr = curr.children[ci]
        
        if not curr or not curr.ending:
            return False
        return True

