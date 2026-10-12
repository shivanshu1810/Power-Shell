"""Password generator: strong temporary passwords for new user onboarding.

Usage:
    python password_generator.py          (one 14-character password)
    python password_generator.py 16 5     (five passwords, 16 characters each)
"""
import secrets  # secrets is made for passwords; random is not
import string
import sys


def make_password(length=14):
    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%&*?",
    ]
    # Start with one character from each group so every rule is met
    chars = [secrets.choice(group) for group in groups]
    # Fill the rest from all groups combined
    pool = "".join(groups)
    chars += [secrets.choice(pool) for _ in range(length - len(chars))]
    # Shuffle so the first four characters aren't predictable
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main():
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    if length < 8:
        print("Use at least 8 characters.")
        return
    for _ in range(count):
        print(make_password(length))
    print("Tip: have the user change it at first sign-in.")


if __name__ == "__main__":
    main()
