class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        j = 0
        alphanum = (''.join(filter(str.isalnum, s))).lower()
        array_s = list(alphanum)
        
        for i in reversed(array_s):
            if i != array_s[j]:
      
                return False
            j+=1
        return True