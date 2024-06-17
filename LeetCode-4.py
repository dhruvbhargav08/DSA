# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        res = []
        n1,n2 = 0,0
        N1,N2 = len(num1),len(num2)
        while n1<N1 and n2<N2:
            if num1[n1]<=num2[n2]:
                res.append(num1[n1])
                n1 += 1
            else:
                res.append(num2[n2])
                n2 += 1
        while n1<N1:
            res.append(num1[n1])
            n1 += 1
        while n2<N2:
            res.append(num2[n2])
            n2 += 1
        resLength = len(res)
        if resLength%2:
            return float(res[resLength//2])
        else:
            return (float(res[resLength//2-1])+float(res[resLength//2]))/2.0
