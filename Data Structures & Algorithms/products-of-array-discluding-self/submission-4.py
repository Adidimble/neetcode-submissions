class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        ans.append(1)
        prefix,postfix = 1,1
        for i in range(1,len(nums)):
            prefix = prefix*nums[i-1]
            ans.append(prefix)

        for i in range(len(nums)-2,-1,-1):
            postfix = postfix*nums[i+1]
            ans[i] *= postfix

        return (ans)
