class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for ele in nums:
           map[ele] =  map.get(ele,0) + 1
        result = sorted(map,key =map.get, reverse =True )
        return result[:k]