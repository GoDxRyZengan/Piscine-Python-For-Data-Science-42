import sys
import ft_filter

def main():
    assert len(sys.argv) == 3, 'the arguments are bad'
    try:
        number = int(sys.argv[2])
    except ValueError:
        raise AssertionError ("the arguments are bad") from None
    words = [x for x in sys.argv[1].split()]
    result = ft_filter.ft_filter((lambda x: len(x) > number), words)
    print(list(result))

if __name__ == "__main__":
    sys.exit(main())