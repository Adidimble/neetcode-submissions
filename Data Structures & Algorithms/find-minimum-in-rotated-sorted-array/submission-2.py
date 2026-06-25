class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0 , len(nums)-1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1   # pivot is in the RIGHT half
            else:
                r = m       # pivot is in the LEFT half (or is m itself)
        return(nums[l])