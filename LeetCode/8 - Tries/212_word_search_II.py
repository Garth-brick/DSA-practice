from typing import Dict, List, Optional

# I WILL COME BACK FOR YOU AFTER I AM DONE WITH WORD SEARCH-1 

""" NOTES 
- I think we can maintain a trie to look for words and do a dfs if we keep finding words
- We will also need a 2D array to keep track of letters we have already used up
- 
"""


class TrieNode:
    
    def __init__(self) -> None:
        self.children: Dict[str, 'TrieNode'] = {}
        self.isEndOfWord: bool = False


class Trie:
    
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str):
        current: TrieNode = self.root
        
        for c in word:
            if c not in current.children.keys():
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isEndOfWord = True
        
    def search(self, word: str):
        current: TrieNode = self.root
        
        for c in word:
            if c not in current.children.keys():
                return False
            current = current.children[c]
        return current.isEndOfWord
    
    def nextLetter(self, prefix: str = "") -> List[str]:
        current: TrieNode = self.root
        
        for c in prefix:
            if c not in current.children.keys():
                return []
            current = current.children[c]
        return list(current.children.keys())
        

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    return []



print(findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))