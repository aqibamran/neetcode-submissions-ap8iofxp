class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        result = []
        for s in strs:
            if str(sorted(s)) in dicts:
                dicts[str(sorted(s))].append(s)
            else:
                dicts[str(sorted(s))] = [s]
        
        for v in dicts.values():
            result.append(v)
        return result