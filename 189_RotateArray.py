# Problem: https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Slower
        # for i in range(k % len(nums)):
        #     temp = nums[-1]
        #     for i in range(len(nums)-1, 0, -1):
        #         nums[i] = nums[i-1]
        #     nums[0] = temp
        
        # Faster
        l = len(nums)
        k = k % l
        left = nums[l-k:]
        right = nums[:l-k]
        
        i = 0
        for n in left:
            nums[i] = n
            i += 1
        for n in right:
            nums[i] = n
            i += 1