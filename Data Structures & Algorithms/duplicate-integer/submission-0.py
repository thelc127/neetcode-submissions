class Solution:
    def hasDuplicate(self, nums:List[int]) -> bool:
        #defining empty set to store seen numbers
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
         