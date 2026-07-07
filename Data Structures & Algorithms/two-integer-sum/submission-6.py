class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}

        for i,num in enumerate(nums):
            map1[num] = i

        for i, num in enumerate(nums):
            second_num = target-num
            if second_num in map1 and i != map1[second_num] :
                return [i,map1[second_num]]