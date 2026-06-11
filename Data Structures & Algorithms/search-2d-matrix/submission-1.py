class Solution:
    def binary(self,target,arr):
        s = 0
        e = len(arr)-1

        while s<=e:
            mid = (s+e)//2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                e = mid -1
            else:
                s= mid+1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            print(arr)
            if self.binary(target,arr):
                return True
        
        return False