class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need={}   #frequency of s1
        freq={} #frequency of s2
        left=0

        for c in range(len(s1)):

            need[s1[c]]=need.get(s1[c],0)+1

        
        for right in range(len(s2)):

            freq[s2[right]]=freq.get(s2[right],0)+1


            if right-left+1>len(s1):

                freq[s2[left]]-=1

                if freq[s2[left]]==0:
                    del freq[s2[left]]
                
                left+=1
            
            if need==freq:
                return True
        return False



        