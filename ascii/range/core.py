SMALL_A_CODE = ord('a')
SMALL_Z_CODE = ord('z')

def asciiRange(start: str, end: str) -> str:
    if len(start) != 1 or len(end) != 1:
        return ''

    startCode = ord(start)
    endCode = ord(end)

    if not (SMALL_A_CODE <= startCode <= SMALL_Z_CODE):
        return ''

    if not (SMALL_A_CODE <= endCode <= SMALL_Z_CODE):
        return ''

    result: list[str] = []

    codeIterator = range(
        min(startCode, endCode),
        max(startCode, endCode) + 1,
    )

    for code in codeIterator:
        result.append(chr(code))

    if startCode >= endCode:
        result.reverse()

    return ''.join(result)
