class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #creating a hashmap
       freq_map = {}
       for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
       sorted_hashmap = sorted(freq_map.keys(), key = lambda x:freq_map[x], reverse = True)

       return sorted_hashmap[:k]
       
    