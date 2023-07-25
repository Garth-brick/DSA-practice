def longestPalindrome(s: str) -> str:

    def isPalindrome(substring) -> bool:
        l = 0
        r = len(substring) - 1
        while l < r:
            if substring[l] != substring[r]:
                return False
            l += 1
            r -= 1
        return True
    
    # {letter: {set of indexes of ocurrence}}
    mp = {}

    result = ""

    for i, char in enumerate(s):
        if char not in mp:
            mp[char] = set()
        mp[char].add(i)	
        for index in mp[char]:
            substring = s[index : i+1]
            if len(substring) > len(result) and isPalindrome(substring):
                result = substring
    return result

print(longestPalindrome("aaca"))