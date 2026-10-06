import sys

if len(sys.argv) <= 1:
    sys.exit()
assert len(sys.argv) <= 2, 'more than one argument is provided'
try:
    number = int(sys.argv[1])
except ValueError:
    raise AssertionError ("argument is not an integer") from None
if (number % 2 != 0):
    print("I'm Odd.")
else:
    print("I'm Even.")
