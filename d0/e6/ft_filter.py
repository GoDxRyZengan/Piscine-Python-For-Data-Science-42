import sys

def ft_filter(function, iterable) -> iter:
    """function to replicater filter"""
    if (function is None):
        return iter([x for x in iterable if x])
    return iter([x for x in iterable if function(x)])

def main():
    number = [1, 2, 3, 4]
    print(type(filter(lambda x: x*2, number)))
    print(type(ft_filter(lambda x: x*2, number)))
    return 0
if __name__ == "__main__":
    sys.exit(main())