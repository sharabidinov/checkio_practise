# Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it,
# function should return True.

def is_all_upper(text: str) -> bool:
    return text == text.upper()


print(is_all_upper('ALL UPPER'))
print(is_all_upper(''))
print(is_all_upper('all lower'))
print(is_all_upper('   '))
print(is_all_upper('234 23'))