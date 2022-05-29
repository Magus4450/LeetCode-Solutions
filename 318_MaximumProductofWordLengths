# Problem: https://leetcode.com/problems/maximum-product-of-word-lengths

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        
        """
        First: Converting each words into a state such as

        'a' = '1 0 0 0 ... 0'
        'abc' = '1 1 1 0 ... 0'
        'cba' = '1 1 1 0 ... 0'

        After doing so, we can check if two words have same letters by using the AND operator.
        If AND operators results in 0, the words do not have same letters

        Second: Iterate through each state and find maximum product of word lengths

        Time Complexity : O(n^2)
        """
        state = []
        for w in words:
            st = 0
            for c in w:
                index = ord(c) - ord('a')
                st |= 1 << index # Or equals to left wise 
            state.append(st)
        
        leng = len(words)
        maxP = 0
        for i in range(leng):
            for j in range(leng):
                if state[i] & state[j] == 0:
                    if len(words[i]) * len(words[j]) > maxP:
                        maxP = len(words[i]) * len(words[j])
        return maxP
                