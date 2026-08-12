class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset =set()
        best = 0
        window = []
        left = 0
        for right in range(len(s)):
            if s[right] not in hashset:
                best = max(best,right -left +1)

                window.append(s[right])
                hashset.add(s[right])
            else:
                while s[right] in hashset:
                    ele = window.pop(0)
                    hashset.remove(ele)
                    left +=1
                best = max(best,right -left +1)

                window.append(s[right])
                hashset.add(s[right])
        
        return best


        