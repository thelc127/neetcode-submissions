class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        #since we need value and index so using enumerate
        for i, n in enumerate(nums):
            diff = target - n
            # meaning the two numbers (n and hashmap value) add to target

            if diff in hashmap:
                # we need indices of those numbers, not values themselves
                # also we need **smaller index first** on the output

                return [hashmap[diff], i]
            
            #update the hashmap with the new values
            hashmap[n] = i
            
            
            
 