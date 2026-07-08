from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            key_map = [0]*26
            for c in s:
                key_map[ord(c)-ord('a')] +=1
            output[tuple(key_map)].append(s)
        
        return(list(output.values()))