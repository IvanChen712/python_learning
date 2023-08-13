def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
