def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

strings = [
    "9847255590886266818998186626880955527489",
    "6892149109325320763773670235239019412986",
    "6800923757255865070000705685527573290086",
    "1414884937242655719669145562427394884141"
]

for string in strings:
    if not palindrome(string):
        print(f"{string} Answer")