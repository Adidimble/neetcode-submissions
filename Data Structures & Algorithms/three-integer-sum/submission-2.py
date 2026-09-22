class Solution:
    def twosum(self, nums, target):
        start, end = 0, len(nums) - 1
        ans = []

        while start < end:
            total = nums[start] + nums[end]

            if total == target:
                ans.append([nums[start], nums[end]])

                # Skip duplicates
                while start < end and nums[start] == nums[start + 1]:
                    start += 1

                while start < end and nums[end] == nums[end - 1]:
                    end -= 1

                start += 1
                end -= 1

            elif total > target:
                end -= 1

            else:
                start += 1

        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            output = self.twosum(nums[i + 1:], -nums[i])

            for pair in output:
                ans.append([nums[i], *pair])

        return ans