import re


def try_regex():
    expr = r"\w+"
    test_str = input("No more string >:)")
    match = re.search(expr, test_str)
    print(
        f"The expression matched {match[0]}"
        if match
        else "There was no match :("
    )


if __name__ == "__main__":
    try_regex()
