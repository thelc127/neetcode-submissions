class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp , rp = 0, len(numbers) - 1

        currentsum = 0

        while lp < rp:
            currentsum = numbers[lp] + numbers[rp]

            #sum is equal to target
            if currentsum == target:
                return [lp+1, rp+1]

            #sum is less than target
            elif currentsum < target: 
                lp +=1

            #sum is greater than target (currentsum > target)
            else:
                rp -=1
        

        # return [lp, rp]


