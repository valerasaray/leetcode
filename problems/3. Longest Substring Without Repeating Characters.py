class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        for i in range(len(s)):
            counter = 0
            characters = []
            for j in range(i, len(s)):
                if s[j] in characters:
                    if counter > max_count:
                        max_count = counter
                    break
                else:
                    counter += 1
                    characters.append(s[j])
                    if j == len(s) - 1:
                        if counter > max_count:
                            max_count = counter     
        return max_count

s = Solution()
print(s.lengthOfLongestSubstring("abc"))