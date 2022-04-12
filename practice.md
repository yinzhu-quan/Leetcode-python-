# Leetcode

#### 2022.04.12

215. Kth Largest Element in an Array

`
     def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def partition(l, r):
            pivot = nums[r]  # always choose the rightmost 
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            return p
`
