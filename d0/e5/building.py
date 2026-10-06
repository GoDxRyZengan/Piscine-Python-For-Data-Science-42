import sys

def main() -> int:
    """Fonction main pour compter les types de caracteres dans une string """
    assert len(sys.argv) <= 2, 'more than one argument is provided'
    if len(sys.argv) <= 1:
        print("What is the text to count?")
        line = sys.stdin.readline()
    else:
        line = sys.argv[1]
    ponctuation = r"""[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"""
    spe = '\n'
    upper, lower, punct, spc, dgt, total = 0, 0, 0, 0, 0, 0
    for char in line:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            dgt += 1
        elif char.isspace():
            spc += 1
        elif char in ponctuation:
            punct += 1
        elif char is spe:
            spc += 1
        
        total += 1
    print("The text contains", total, "characters")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punct, "punctuation marks")
    print(spc, "spaces")
    print(dgt, "digits")
    return 0

if __name__ == "__main__":
    sys.exit(main())