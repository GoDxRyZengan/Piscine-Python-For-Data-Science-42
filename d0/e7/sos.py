import sys

LETTERS_MORSE = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    " ": "/ ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}

def main():
    """programme pour passer une string en morse"""
    assert len(sys.argv) == 2, 'the arguments are bad'
    result = ""
    for char in sys.argv[1]:
        if char.isalnum() or char.isspace():
            result += LETTERS_MORSE[char.upper()]
        else:
            assert False, 'the arguments are bad'
    print(result)
    return 0

if __name__ == '__main__':
    sys.exit(main())