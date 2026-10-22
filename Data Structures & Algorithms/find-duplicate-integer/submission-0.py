class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use the array's values as index pointers to form a Linked List:
        # Input Array: nums = [1, 2, 3, 2, 2]
        # Indices:            0  1  2  3  4
        #
        # Node-to-Node Transitions (Index -> nums[Index]):
        # Index 0 (Value 1) -> jumps to Index 1
        # Index 1 (Value 2) -> jumps to Index 2
        # Index 2 (Value 3) -> jumps to Index 3
        # Index 3 (Value 2) -> loops back to Index 2  <-- Cycle starts here!
        # Index 4 (Value 2) -> jumps to Index 2       <-- Separate branch into the cycle
        # Why this works: Because 2 is the duplicate value, multiple indices (1, 3, and 4) 
        # point to Index 2. This convergence forms the entrance of the cycle.

        fast, slow = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow2
