class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_count = 1
        maj_num = nums[0]

        for num in nums[1:]:
            if maj_count == 0:
                maj_num = num 
            if num == maj_num: 
                maj_count += 1
            else: 
                maj_count -=1
        return maj_num


"""
Input: 
maj_count = -1
maj_num = 1
                  i
nums = [5,5,1,1,1,5,5]


"""