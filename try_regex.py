import re


expr = r"\w+"
test_str = input("Give me a string: ")
match = re.search(expr, test_str)
print(
    f"The expression matched {match[0]}"
    if match
    else "There was no match :("
)
