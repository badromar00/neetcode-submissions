class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n


        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        res = [1] * n
        for i in range(n):
            res[i] = postfix[i] * prefix[i]
        return res



"""
              i
nums =    [1, 2, 4, 6]

prefix = 

postfix = [48, 24, 6, 1]




res =.  = []


"""
        