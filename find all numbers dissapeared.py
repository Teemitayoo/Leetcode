class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        app = [i for i in range(1,len(nums)+1)]
        nothing = []
        for n in app:
              if n not in nums:
                 nothing.append(n)
        return nothing
