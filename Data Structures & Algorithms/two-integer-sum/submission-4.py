class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_map = {}

        for i, num in enumerate(nums):
            pos_map[num] = i
        
        for i,num in enumerate(nums):
            needed = target -num
            if needed in pos_map and i != pos_map[needed]:
                return [i,pos_map[needed]]
        
        return None