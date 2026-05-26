class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxLen = 0        

        for ele in setNums:
            
            if ele-1 not in  setNums:
                localLen = 1
                while True:
                    ele = ele+1
                    if ele in setNums:
                        localLen+=1
                    else:
                        break

                if localLen>maxLen:
                    maxLen = localLen
        
        return maxLen
                    
