import heapq
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        k = len(nums) - k

        def partition(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            return p

        def select(l, r):
            p = partition(l, r)
            if k < p:
                return select(l, p-1)
            elif k > p:
                return select(p+1, r)
            else:
                return nums[p]
        return select(0, len(nums)-1)

if __name__ == '__main__':
    s = Solution()
    nums, k = [3, 2, 1, 5, 6, 4], 2
    ans = s.findKthLargest(nums, k)
    print(ans)
