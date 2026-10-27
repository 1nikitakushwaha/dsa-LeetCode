class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            else:
                break

        return k
        # low = 0
        # high = len(arr) - 1

        # while low <= high:

        #     mid = (low + high) // 2

        #     missing = arr[mid] - (mid + 1)

        #     if missing < k:
        #         low = mid + 1
        #     else:
        #         high = mid - 1

        # return low + k