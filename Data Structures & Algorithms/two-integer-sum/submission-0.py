class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #creating a hashmap to store the number(n, in array) and its index i
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i