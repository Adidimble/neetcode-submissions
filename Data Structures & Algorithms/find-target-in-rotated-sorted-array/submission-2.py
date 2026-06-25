class Solution:
    def binary_search(self,l,r,nums,target):
        while l <=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1

# Find the pivot so that we can apply the Binary Search to both the halves
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums)-1
        
        #Find the pivot compare the mid with the right if mid > r then ans will be in the right half 
        # if mid < r then the ans will be in the left half ,
        # lowest / min element will be the pivot so pivot = l
        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r= mid
        pivot = l

        ans = self.binary_search(0,pivot-1,nums,target)
        if ans!=-1:
            return ans
        return self.binary_search(pivot,len(nums)-1,nums,target)
                
        

        