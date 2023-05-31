class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        dict={}
        for i , num in enumerate(nums):
            c=target-num
            if c in dict:
                return [dict[c],i]
            else:
                dict[num]=i
        return []