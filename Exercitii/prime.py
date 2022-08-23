import math

def previous_is_prime(second):
    first = second - 1

    if first == 2:
        return True
    if first % 2 == 0 or first <= 1:
        return False

    sqr = int(math.sqrt(first)) + 1

    for divisor in range(3, sqr, 2):
        if first % divisor == 0:
            return False
    return True

print(previous_is_prime(9))