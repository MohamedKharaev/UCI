#Mohamed Kharaev 21970006736499 and _______. ICS 31 Lab sec 7.
def factorial(n: int) -> int:
    ''' Compute n! (n factorial) '''
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)
assert factorial(0) == 1
assert factorial(5) == 120

print("10! is", factorial(10))
print("100! is", factorial(100))
