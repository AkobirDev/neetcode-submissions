class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        len1 = len(word1)
        len2 = len(word2)

        result = ''

        while i < len1 and j < len2:
            result += word1[i] + word2[j]
            i += 1
            j += 1
        
        if i < len1:
            result += word1[i:]
        
        if j < len2:
            result += word2[j:]
        
        return result