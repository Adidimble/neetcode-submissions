class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        hashset = set()
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left+=1

            best = max(best,right-left+1)
            hashset.add(s[right])

        return best
