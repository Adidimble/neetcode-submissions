class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(ch.lower() for ch in s if ch.isalnum())     
        
        start = 0
        end =len(cleaned_s) - 1

        while start <end:
            if cleaned_s[start] != cleaned_s[end]:
                return False
            start += 1
            end -= 1

        return True