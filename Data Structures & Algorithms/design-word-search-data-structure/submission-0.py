class TrieNode:

    def __init__(self):

        self.children = [None] * 26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):

        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        curr = self.root
        for letter in word:

            index = ord(letter) - ord('a')

            if not curr.children[index]:
                curr.children[index] = TrieNode()
            
            curr = curr.children[index]
        
        curr.isLeaf = True
        

    def search(self, word: str) -> bool:

        def dfs(node, iteration):

            if iteration == len(word):
                return node.isLeaf

            letter = word[iteration]

            if letter == '.':

                for child in node.children:

                    if child and dfs(child, iteration + 1):
                        return True
                return False
            
            child = node.children[ord(letter) - ord('a')]

            return child is not None and dfs(child, iteration + 1)
        
        return dfs(self.root, 0)

'''

tried to do linear should do dfs instead
        curr = self.root
        for letter in word:

            if letter == '.':
                for other in curr.children:
                    if other:
            

            if not curr.children[index]:
                return False
            
            curr = curr.children[index]
        
        return curr.isLeaf
'''