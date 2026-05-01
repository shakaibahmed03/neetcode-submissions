class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        freq={}

        for st,ts in zip(s,t):
            freq[st]=freq.get(st,0)+1
            freq[ts]=freq.get(ts,0)-1
        
        return all(x==0 for x in freq.values())


        

        