class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_substring_size = 0
        letter_counts = {}
        l_ptr = 0
        r_ptr = 0
        max_letter_freq = 0

        while r_ptr < len(s):
            # print("l_ptr is: " + str(l_ptr) + " r_ptr is: " + str(r_ptr))
            window_size = r_ptr - l_ptr + 1

            # Make sure counts are updated BEFORE checking validity, this always must happen
            if s[r_ptr] in letter_counts:
                letter_counts[s[r_ptr]] = letter_counts[s[r_ptr]] + 1
            else:
                letter_counts[s[r_ptr]] = 1
            max_letter_freq = max(max_letter_freq, letter_counts[s[r_ptr]])
            r_ptr += 1

            if (window_size - max_letter_freq <= k):
                # print("valid substring")
                max_substring_size = max(max_substring_size, window_size)
            else:
                # print("no longer valid, had to shift l_ptr")
                letter_counts[s[l_ptr]] -= 1
                l_ptr += 1

        return max_substring_size
        