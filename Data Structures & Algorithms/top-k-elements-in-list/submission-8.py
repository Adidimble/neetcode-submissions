class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []

        for ele in nums:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1
        
        new_map = dict(sorted(map.items(),key = lambda item:item[1]))
        while k:
            print(map)
            result.append(new_map.popitem()[0])
            k-=1

        return result