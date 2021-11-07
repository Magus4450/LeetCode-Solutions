# Problem: https://leetcode.com/problems/first-bad-version/


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        low, high = 0, n
        
        while low <= high:
            mid = (low+high) // 2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid):
                high = mid - 1
            elif not isBadVersion(mid):
                low = mid + 1
        