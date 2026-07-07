class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        if len(s) != len(t):
            return False
        for s, t in zip(s,t):
            map1[s] = map1.get(s,0)+1
            map2[t] = map2.get(t,0)+1
        
        if map1 != map2:
            return False
        return True