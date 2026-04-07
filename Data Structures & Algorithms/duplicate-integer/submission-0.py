class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         dup = []
         for i in nums:
            if i not in dup:
                dup.append(i)
            else:
                return True
         return False