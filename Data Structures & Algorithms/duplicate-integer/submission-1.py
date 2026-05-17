class Solution:
    def hasDuplicate1(self, nums: List[int]) -> bool:
        number_map = {}
        for num in nums:
            if num in number_map:
                return True
            else:
                number_map[num]=1
        return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))