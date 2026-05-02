class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}

        for n in nums:
            freq[n]=freq.get(n,0)+1
        
        buckets=[[] for _ in range(len(nums)+1)]

        for m,v in freq.items():
            buckets[v].append(m)
        
        
        res=[]
        for s in reversed(buckets):
            res.extend(s)
            if len(res)==k:
                return res
        
        

        