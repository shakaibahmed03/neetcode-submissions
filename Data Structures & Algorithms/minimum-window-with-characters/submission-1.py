class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # need= frequency of t
        # window=frequency of s
        
        #in t.      have=how many characters currently satisfied
        #in t.      need_count= total unique rrequired chars

        need={}
        for n in t:
            need[n]=need.get(n,0)+1
        
        l=0
        window={}

        have=0
        need_count=len(need)
        
        res=[-1,-1]
        reslen=float('inf')

        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1

            

        
            if s[right] in need and window[s[right]]==need[s[right]]:
                have+=1

                #shrink while valid
                while have==need_count:
                    if (right-l+1)<reslen:
                        reslen=right-l+1
                        res=[l,right]

                    window[s[l]]-=1
                    if s[l] in need and window[s[l]]<need[s[l]]:
                        have-=1
                    l+=1
        
        l,right=res
        return s[l:right+1]
                            
            






        

        