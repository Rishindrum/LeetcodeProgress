class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #0(m+n): merge, and then return len//2 or (len//2 + len//2 -1 ) /2

        #find larger and smaller

        #start from the center of larger, index in smaller depending on that

        smaller = nums1
        larger = nums2

        if len(larger) < len(smaller):
            smaller, larger = larger, smaller

        smallLen = len(smaller)
        largeLen = len(larger)

        median = (smallLen+largeLen+1)//2

        left = 0
        right = len(smaller)

        while left <= right:
            mid = (left + right)//2

            smallLeft = smaller[mid - 1] if mid != 0 else float('-inf')
            smallRight = smaller[mid] if mid != smallLen else float('inf')

            largeLeft = larger[median - mid - 1] if (median - mid) > 0 else float('-inf')
            largeRight = larger[median - mid] if median - mid < largeLen else float('inf')

            if largeLeft > smallRight:
                left = mid + 1
            elif smallLeft > largeRight:
                right = mid - 1
            else:
                if (smallLen + largeLen) % 2 == 0:
                    print(largeLeft, smallLeft)
                    return (max(largeLeft, smallLeft) + min(largeRight, smallRight))/2
                else:
                    return max(largeLeft, smallLeft)


        





        