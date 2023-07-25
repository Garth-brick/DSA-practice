from typing import List


def isPalindrome(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True
            
            
def palindromePartition(s: str) -> List[List[str]]:
    result: List[List[str]] = []
    
    def backtrack(chosenStrings: List[str], startIndex: int) -> None:
        
        if startIndex >= len(s):
            result.append(chosenStrings)
            return
        
        for i in range(startIndex, len(s)):
            substring = s[startIndex:(i + 1)]
            
            if isPalindrome(substring):
                backtrack(chosenStrings + [substring], i + 1)
    
    backtrack([], 0)
    return result

print(palindromePartition("aab"))