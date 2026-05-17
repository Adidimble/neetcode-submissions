class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
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

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen = {}

        for n in s:
            seen[n]=seen.get(n,0)+1
        
        for n in t:
            if n not in seen:
                return False
            seen[n]-=1
            if seen[n]==0:
                del seen[n]
        return True
        