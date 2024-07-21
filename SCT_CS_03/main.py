import re

def password(passwd):
    strength = 0
    char_size = 0
    if re.search(r'[a-z]', passwd):
        char_size += 26
        strength += 1

    if re.search(r'[A-Z]', passwd):
        char_size += 26
        strength += 1

    if re.search(r'\d', passwd):
        char_size += 10
        strength += 1

    if re.search(r'[!@#$%^&*()-_=+{};:"|,<.>/?]', passwd):
        char_size += 32
        strength += 1

    if len(passwd) >= 8:
        strength += 1
    combinations = char_size ** len(passwd)
    estimated_time(combinations)

    return strength


# Finding how much hours will it take to crack the password
def estimated_time(combinations):
    guess_per_second = 1e9  # 1 billion guess per second
    guess_time = combinations / guess_per_second  # in seconds
    time_in_hours = guess_time / (60 * 60)
    print(f"Time to crack you password is   :   {time_in_hours} seconds")


if __name__ == "__main__":
    st = input("Enter password  :   ")
    strength = password(st)
    if strength == 5:
        print("Password strength is  :   STRONG")
    elif strength >= 3:
        print("Password strength is  :   MEDIUM")
    else:
        print("Password strength is  :   LOW")
