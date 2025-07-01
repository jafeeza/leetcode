class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before_pivot=[x for x in nums if x<pivot]
        after_pivot=[x for x in nums if x>pivot]
        pivot_arr=[x for x in nums if x==pivot]
        return before_pivot+pivot_arr+after_pivot