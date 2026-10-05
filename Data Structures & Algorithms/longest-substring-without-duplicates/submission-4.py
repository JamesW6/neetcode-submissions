class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        input: string s
        output: length of longest substring

        constraints: s can be any length
        s can hold any ascii characters

        ideas:
        keep index of last duplicate
        keep current length of long substring
        iterate through the array, when we find a new duplicate,
        the length resets to 0
        '''

        length=0
        longest=0
        seen={}
        reset=0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]]>=reset:
                longest=max(longest,length)
                length=i-seen[s[i]]
                reset=seen[s[i]]
            else:
                length+=1
            seen[s[i]]=i
        return max(longest,length)