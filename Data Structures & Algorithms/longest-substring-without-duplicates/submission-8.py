class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        rp = -1
        max_sub = 0
        visited = defaultdict(int)
        for char in s:
            rp += 1
            print(f"INITIAL STATE: {s[lp:rp + 1]}, lp = {lp}, and rp = {rp}")
            if (visited[char] == 0):
                max_sub = max(max_sub, rp - lp + 1)
            else:
                print(f"FLAG")
                
                while (visited[char] != 0):
                    visited[s[lp]] -= 1
                    lp += 1

            visited[char] += 1

            print(f"FINAL STATE: {s[lp:rp + 1]}, lp = {lp}, and rp = {rp}")

        return max_sub
