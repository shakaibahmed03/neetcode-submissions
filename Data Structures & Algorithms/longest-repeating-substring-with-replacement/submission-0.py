class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        best=0
        freq={}
        maxf=0

        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            maxf=max(maxf,freq[s[right]])

            while (right-left+1)-maxf>k:

                freq[s[left]]-=1

                if freq[s[left]]==0:
                    del freq[s[left]]
                
                left+=1
            
            best=max(best, right-left+1)
        
        return best
        