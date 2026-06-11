class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        # code here
        parts = []
        for i in range(0, len(s), k):
            parts.append(s[i:i+k])
        freq = {}
        for part in parts:
            if part in freq:
                freq[part] += 1
            else:
                freq[part] = 1
        if len(freq) == 1:
            return True
        if len(freq) == 2:
            for value in freq.values():
                if value == 1:
                    return True
        return False        
