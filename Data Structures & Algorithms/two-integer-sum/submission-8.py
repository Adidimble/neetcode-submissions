class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_of_nums = {}
        for i,num in enumerate(nums):
            print(i,num)
            map_of_nums[num] = i

        for i, num in enumerate(nums):
            second_num = target-num
            if second_num in map_of_nums and i!= map_of_nums[second_num]:
                return [i,map_of_nums[second_num]]     
