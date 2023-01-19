def append_if_not_in_list(letter: chr, char_list: list) -> None:
    '''Function appending letter to existing list if that letter (character) is not a part of that list'''
    if letter not in char_list:
        char_list.append(letter)


def chars_checker(S: str) -> tuple:
    '''Return tuple of 2 lists: first with index 0 with all lowercase characters in given string and second with index 1
       with all uppercase characters from that string.'''
    lower_chars = []
    upper_chars = []
    for letter in S:
        if letter.isupper():
            append_if_not_in_list(letter, upper_chars)
        else:
            append_if_not_in_list(letter, lower_chars)
    return lower_chars, upper_chars


def is_string_balanced(lower_chars: list, upper_chars: list) -> bool:
    '''Returns True if there are the exactly the same characters in two given lists, one of lower and second of
    uppercase characters.
    Returns False in other cases.'''
    if len(lower_chars) == len(upper_chars):
        for lower_char in lower_chars:
            if lower_char.upper() not in upper_chars:
                return False
        return True
    else:
        return False


def solution(S: str):
    '''Returns length of the shortest string slice that is a balanced string or -1 if there is no balanced string
       in given series of characters'''
    for i in range(2, len(S) + 1):
        slice_start = 0
        for j in range(len(S) - i + 1):
            slice = S[slice_start:slice_start+i]
            slice_start += 1
            lowers, uppers = chars_checker(slice)
            if is_string_balanced(lowers, uppers):
                return len(slice)
            else:
                continue
    return -1

print(solution('ZdRXXDxzr'))
