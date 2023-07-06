from typing import List, Optional, Dict
from collections import defaultdict

""" NOTES
- We need to create a tree which goes from the first letter to the last letter
- Each node could potentially have 26 children (one for each letter)
- We will need a dummy root node to store all the characters that a word can start from
- We will also need to mark the ends of words to be able to search for them effectively
"""


class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.__isEndOfWord = False
        
    @property
    def isEndOfWord(self) -> bool:
        return self.__isEndOfWord

    def setEndOfWord(self, value: bool) -> None:
        self.__isEndOfWord = value


class PrefixTree:
    def __init__(self) -> None:
        self.__wordCount: int = 0
        self.__dummyRoot: TrieNode = TrieNode()
        self.__dummyRoot.setEndOfWord(True)
        
    @property
    def __root(self):
        return self.__dummyRoot
    
    @property
    def getWordCount(self):
        return self.__wordCount
    
    def __incrementWordCount(self) -> None:
        self.__wordCount += 1
        
    def __decrementWordCount(self) -> None:
        assert self.getWordCount > 0, "word count can't go below zero"
        self.__wordCount -= 1

    def insert(self, word: str) -> None:
        current: TrieNode = self.__root
        
        for c in word:
            if c not in current.children.keys():
                current.children[c] = TrieNode()
            current = current.children[c]
            
        if not current.isEndOfWord:
            current.setEndOfWord(True)
            self.__incrementWordCount()
        else:
            print("value was already present")
            

    def search(self, word: str) -> bool:
        current: TrieNode = self.__root
        
        for c in word:
            if c not in current.children.keys():
                return False
            current = current.children[c]
        return current.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        current: TrieNode = self.__root
        
        for c in prefix:
            if c not in current.children.keys():
                return False
            current = current.children[c]
        return True
    
    # returns True if the word was present and removed, False otherwise
    def remove(self, word: str) -> bool:
        
        """ APPROACH 
        - Check if the word exists by traversing down the trie
        - If the word doesn't exist then return False
        - If the word exists, keep a stack of all the TrieNodes after the last one which was the end of another word and unlink all the TrieNodes in the stack uptil the node that is an end of word or the root itself
        """
        
        if not word: return False
        
        stack: List[TrieNode] = []
        current: TrieNode = self.__root
        
        for c in word:
            if c not in current.children.keys():
                return False
            current = current.children[c]
            stack.append(current)
        
        if not current.isEndOfWord:
            return False
        
        i: int = 1
        while stack:
            stack[-(i+1)].children.pop(word[-i])
            if stack[-(i+1)].isEndOfWord:
                break
            i += 1
        return True
        
    
    
pt = PrefixTree()
pt.insert("apple")
pt.insert("apple")
print(pt.getWordCount) # 1
print(pt.search("apple")) # True
print(pt.search("app")) # False
print(pt.startsWith("ap")) # True
pt.insert("app") 
print(pt.getWordCount) # 2
print(pt.search("app")) # True
pt.remove("apple")
print(pt.search("app")) # True