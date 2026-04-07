class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s, t):
            if len(s) != len(t):
                return False
            return Counter(s) == Counter(t)
        
        res = []

        i = 0
        while i < len(strs):
            new = [strs[i]]
            j = i+1
            while j < len(strs):
                if is_anagram(strs[i], strs[j]):
                    new.append(strs[j])
                    strs.pop(j)
                    j -= 1
                j += 1
            res.append(new)
            i += 1;
        
        return res
