def max_digit(number: int) -> int:
    lst = [int(digit) for digit in str(number)]
    return max(lst)
