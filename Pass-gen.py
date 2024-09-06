# This is random password generator

import random
import string


def input_length():
    try:
        amount = int(input("number of passwords to be generated: "))
        length = int(input("length of each password: "))
    except ValueError:
        print("\nplease provide valid numerical values!\n")
        input_length()
    return [
        "".join(
            random.choices(
                string.ascii_letters + string.digits + string.punctuation, k=length
            )
        )
        for password in range(amount)
    ]


passwords = input_length()
print("\ngenerated passowrds:\n")
for password in passwords:
    print(password, "\n")
