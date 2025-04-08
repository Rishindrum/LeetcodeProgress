class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        right = n - 1

        while left<=right:
            mid = (left+right)//2

            if nums[mid] <= nums[(mid+1)%n] and nums[mid] <= nums[(mid-1)%n]:
                return nums[mid]
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        

        