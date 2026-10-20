class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            freq[index] += 1

            max_freq = max(max_freq, freq[index])

            if (right - left + 1) - max_freq > k:
                left_index = ord(s[left]) - ord('A')
                freq[left_index] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length