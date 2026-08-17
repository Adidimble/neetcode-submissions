class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        best = 0
        left = 0

        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left +=1
            
            hashset.add(s[right])
            best = max(best,right-left+1)

        return best
