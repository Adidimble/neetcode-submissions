class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        if len(s)!=len(t):
            return False

        for n in s:
            if n in seen_s:
                seen_s[n]+=1
            else:
                seen_s[n]=1

        for n in t:
            if n in seen_t:
                seen_t[n]+=1
            else:
                seen_t[n]=1
        if seen_s == seen_t:
            return True
        return False
        