# Problem: https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums:list[int]) -> list[int]:
        
        
        
        def mergeSort(arr):
            if len(arr) > 1:

                mid = len(arr) // 2

                L = arr[:mid]
                R = arr[mid:]
                
                mergeSort(L)
                mergeSort(R)
                
                i = j = k = 0
                
                while i < len(L) and j < len(R):
                    if L[i]  <= R[j]:
                        arr[k] = L[i]
                        i += 1                        
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                    
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
            return arr
        squared = [x*x for x in nums]
        return mergeSort(squared)
            
            