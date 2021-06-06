class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dic[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        m = len(word)
        for findword in self.dic[m]:
            i = 0
            while i<m and (findword[i] == word[i] or word[i] == "."):
                i+=1
            if i == m:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)