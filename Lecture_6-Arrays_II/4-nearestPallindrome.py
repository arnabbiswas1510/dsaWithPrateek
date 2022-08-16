"""
The approach in this problem is to take half of the num (pallindrome base) for both even and odd lengths of num
Then mirror image this half and build 3 pallindromes, with [base-1, base, base+1]
Then maintain a running diff of abs(num-pallin) for each of the 3 pallindromes above and return the pallin with the smallest diff
"""
def nearestPalindromic(n: str) -> str:
    #First tackle the 2 corner cases of 100 and 99 as below
    if int(n) <= 10 or (
            int(n) % 10 == 0 and int(n[1:]) == 0
    ):  # <= 10 or equal to 100, 1000, 10000, ...
        return str(int(n) - 1)
    elif n[0] == "9" and n[0] * len(n) == n:  # 99, 999, 9999, 99999, ...
        return str(int(n) + 2)
    else: #Main logic
        def build_palindrome(base: str, is_even_length = True) -> str:
            """
            Build a palindrome using the given base.

            e.g.
            build_palindrome("123", True) = "123321"
            build_palindrome("123", False) = "12321"
            """
            if is_even_length:
                return base + ''.join(reversed(base))
            else:
                return base + ''.join(reversed(base[:-1]))

        is_n_even = len(n) % 2 == 0
        palindrome_base = int(n[0: len(n) // 2]) if is_n_even else int(n[0: len(n) // 2 + 1])

        is_n_palindrome = build_palindrome(str(palindrome_base), is_n_even) == n
        #We dont need toinclude palindrome_base if num is already a pallindrome
        base_candidates = [palindrome_base - 1, palindrome_base + 1] if is_n_palindrome \
            else [palindrome_base - 1, palindrome_base, palindrome_base + 1]  # Maintains increasing order

        min_diff = float("inf")
        for base_candidate in base_candidates:
            candidate = int(build_palindrome(str(base_candidate), is_n_even))
            if abs(candidate - int(n)) < min_diff:
                min_diff = abs(candidate - int(n))
                min_base_candidate = str(base_candidate)

        return build_palindrome(min_base_candidate, is_n_even)

print(nearestPalindromic("78936"))