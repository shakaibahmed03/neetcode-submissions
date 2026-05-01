class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups=defaultdict(list)
        for s in strs:
            keys=tuple(sorted(s))
            groups[keys].append(s)
        return list(groups.values())

        