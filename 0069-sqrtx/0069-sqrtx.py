class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        low = 1
        high = x
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans