class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        left = 0
        count = {}
        maxFreq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1

            maxFreq = max(maxFreq,count[s[right]])

            windowLen = right - left +1

            if windowLen - maxFreq >k:
                count[s[left]] -=1
                left+=1
            
            best = max(best,right-left+1)
    
        return best

