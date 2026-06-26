class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we will find the pivot which is essentially  = min 

        l,r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                #the pivot is in the right half
                l = mid+1
            else:
                r= mid
        return nums[l]
