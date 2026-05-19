class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c) - ord('a')] +=1
            
            #using the count map as the key for storing the string in the value
            res[tuple(count)].append(s)
        print(res)
        return list(res.values())