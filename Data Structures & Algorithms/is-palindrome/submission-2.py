class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(ch.lower() for ch in s if ch.isalnum())     
        
        start =0 
        end = len(cleaned_s)
        for i in range(0,(len(cleaned_s)//2)):
            start =0 +i
            end = len(cleaned_s) -i -1
            print(start,end)
            if cleaned_s[start] != cleaned_s[end]:
                return False
        
        return True