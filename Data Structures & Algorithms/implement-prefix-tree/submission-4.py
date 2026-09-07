class TrieNode:

    def __init__(self):

        self.children = [None] * 26
        self.isLeaf = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.root

        for letter in word:

            index = ord(letter) - ord('a') 
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]

        curr.isLeaf = True

    def search(self, word: str) -> bool:

        curr = self.root

        for letter in word:
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                return False

            curr = curr.children[index] # ensures that it's a word and not a prefix
            
        return curr.isLeaf
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for letter in prefix:
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                return False

            curr = curr.children[index] # ensures that it's a word and not a prefix
            
        return True
        
        