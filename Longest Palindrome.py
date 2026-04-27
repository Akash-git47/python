def longest_palindrome(s):
    res, res_len = "", 0

    def expand(l, r):
        nonlocal res, res_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res, res_len = s[l:r+1], r - l + 1
            l -= 1; r += 1

    for i in range(len(s)):
        expand(i, i)      # odd length
        expand(i, i + 1) # even length
    return res

print(longest_palindrome("babad"))   # "bab"
print(longest_palindrome("cbbd"))    # "bb"