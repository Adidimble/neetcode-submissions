class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create freq map
        # sort them
        # take the last k or first k depending on the sorting
        ans = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        sorted_freq = dict(sorted(freq.items(),key = lambda item:item[1]))
        
        while k:
            ele = sorted_freq.popitem()
            ans.append(ele[0])
            k-=1
        return ans
    
        