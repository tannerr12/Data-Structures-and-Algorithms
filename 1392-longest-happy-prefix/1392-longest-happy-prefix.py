class Solution:
    def longestPrefix(self, s: str) -> str:
        

        MOD = 10**9 + 7
        P = 31  # Prime number for polynomial rolling hash

        n = len(s)
        prefix_hashes = [0] * n
        suffix_hash = 0
        max_len = 0
        ppow = 1  # Power of P, initialized for the first character

        # Precompute prefix hashes
        for i in range(n):
            prefix_hashes[i] = ((prefix_hashes[i-1] if i > 0 else 0) * P + ord(s[i]) - ord('a') + 1) % MOD

        # Compare suffix hashes against precomputed prefix hashes
        for i in range(1, n):
            # Update the suffix hash by adding the current character from the end
            # We use ppow to ensure that this character is correctly placed in the hash calculation
            suffix_hash = (suffix_hash + (ord(s[n - i]) - ord('a') + 1) * ppow) % MOD
            ppow = (ppow * P) % MOD  # Update ppow for the next iteration

            # If the current prefix and suffix hashes match, update max_len
            # Note: prefix_hashes[i-1] is the hash of the prefix of length i
            if prefix_hashes[i-1] == suffix_hash:
                max_len = i

        # The longest happy prefix is the substring of s from 0 to max_len
        return s[:max_len]
