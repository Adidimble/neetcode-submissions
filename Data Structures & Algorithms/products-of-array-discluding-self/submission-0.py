class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:      
        result = []
        prefix = 1
        result.append(prefix)

        #prefix array travel in order
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            result.append(prefix)
        
        #postfix travel in reverse order
        postfix= 1
        for i in range(len(nums)-2 ,-1,-1):
            postfix *= nums[i+1]
            result[i]*=postfix

        return result

            