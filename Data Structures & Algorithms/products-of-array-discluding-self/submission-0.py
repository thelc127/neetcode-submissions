class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1] * n

        for i in range(n):
            for j in range(n):

                if i !=j:
                    prod[i] = prod[i] * nums[j]
        return prod

        

    
        