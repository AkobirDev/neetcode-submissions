class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while r >= l:
            if not s[l].isalnum():
                l += 1
                continue
            
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            
            else:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
        
        return True
    
    def isPalindrome(self, s: str, l: int, r: int) -> bool:

        while r >= l:
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True
    


"""
abbadc

"""