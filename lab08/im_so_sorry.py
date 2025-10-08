def blocks(n):
    if n <= 0:
        return 0
    else:
        return blocks(n-1) + n

# recursion runs a loop over and over again by calling the function within itself until a certain criteria is met


def factorial(n):
    if n <= 0:
        return 1
    else:
        return factorial(n-1) * n

# challenge


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

# challenge


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return sum_of_digits(n // 10) + (n % 10)


# challenge
def print_count_down(n):
    if n <= 0:
        print("BOOM")
    else:
        print(n)
        print_count_down(n-1)


# for recursion, there must be a way for the function to not recurse or repeat, so you need a way for it to end.
print_count_down(10)
print(sum_of_digits(415))
print(sum_of_digits(1111))
'''print(is_palindrome("hello"))
print(is_palindrome("racecar"))
print(is_palindrome("tacocat"))
print(blocks(15))
print(blocks(4))
print(factorial(4))
print(len(str(factorial(52))))
print(factorial(8))'''
