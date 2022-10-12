class Trie:
    def __init__(self):
        self.words = {}
        
    def insert(self, word: str) -> None:
        current = self.words
        
        for i in range(len(word)):
            current.setdefault(word[i], {})
            current = current[word[i]]
        
        current["_"] = "_"
    
    def find(self, word:str, findWhole: bool) -> bool:
        current = self.words
        for i in range(len(word)):
            if word[i] in current:
                current = current[word[i]]
            else:
                return False
        
        if not findWhole:
            return True
        if "_" in current:
            return True
        return False
        
    def search(self, word: str) -> bool:
        return self.find(word, True)
        

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, False)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)