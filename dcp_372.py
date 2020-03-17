"""
This problem was asked by Amazon.

Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.
"""


def countDigitsStr(natNum):
    return len(str(abs(natNum)))

print(countDigitsStr(235235234624563454563423))