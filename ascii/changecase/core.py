import __future__

BIG_A_CODE = ord('A')
SMALL_A_CODE = ord('a')
SMALL_Z_CODE = ord('z')

def asciiToUpperCase(string: str) -> str:
    result = []

    for char in string:
        currentCharCode = ord(char)

        if (SMALL_A_CODE <= currentCharCode <= SMALL_Z_CODE):
            code = BIG_A_CODE + currentCharCode - SMALL_A_CODE
            result.append(chr(code))
        else:
            result.append(char)

    return ''.join(result)

