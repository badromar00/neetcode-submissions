class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return l




"""

Input: 
 right always moves
 
 if nums[r] == val then swap. Only l stays
 keep track of number of times current == val


                   l
                       r
Input: nums = [0,1,2,2,3,0,4,2], val = 2

"""