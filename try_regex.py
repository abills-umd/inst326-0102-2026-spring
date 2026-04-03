import re


def try_regex_print():
    print("Let's try a regex!")
    expr = r"^\w+$"
    test_str = input("Give me a string: ")
    match = re.search(expr, test_str)
    print(
        f"The regular expression matched {match[0]}"
        if match
        else "🐹 wowowow"
    )
    
def help():
    print("I don't know what else to add")


if __name__ == "__main__":
    try_regex_print()
