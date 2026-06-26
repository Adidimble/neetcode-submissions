class Solution:
    def binary_search(self,l,r,nums,target):
        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]> target:
                r = mid-1
            else:
                l = mid+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 ,len(nums)-1

        #find the pivot and then apply binary search on both the halves

        while l<r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
            
        pivot = l 

        ans = self.binary_search(0,pivot-1,nums,target)
        if ans !=-1:
            return ans
        return self.binary_search(pivot,len(nums)-1,nums,target)

        