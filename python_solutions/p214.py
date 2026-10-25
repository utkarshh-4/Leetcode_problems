class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse = s[::-1]
        combined = s + "#" + reverse

        lms = [0] * len(combined)

        for i in range(1, len(combined)):
            length = lms[i - 1]

            while length > 0 and combined[i] != combined[length]:
                length = lms[length - 1]

            if combined[i] == combined[length]:
                length += 1

            lms[i] = length

        prefix_len = lms[-1]
        return s[prefix_len:][::-1] + s