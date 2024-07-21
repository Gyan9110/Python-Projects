# Encryption
def encryption(st, shift):
    result = ""
    for i in st:
        if i == " ":
            result += " "
            continue
        if i.isupper():
            result += chr(((ord(i) - ord("A") + shift) % 26) + ord("A"))
        else:
            result += chr(((ord(i) - ord("a") + shift) % 26) + ord("a"))
    print(f"Encrypted text   :   {result}\n")

# Decryption
def decryption(st2, shift2):
    result = ""
    for i in st2:
        if i == " ":
            result += " "
            continue
        if i.isupper():
            result += chr(((ord(i) - ord("A") - shift) % 26) + ord("A"))
        else:
            result += chr(((ord(i) - ord("a") - shift) % 26) + ord("a"))
    print(f"Original Text   :   {result}\n")


# Main Input
if __name__ == "__main__":
    n = 1
    while n != 0:
        choice = int(input("Choose   :   1. Encryption    2.Decryption    3. Exit \n"))
        match choice:
            case 1:
                st = input("Enter text  :   ")
                shift = int(input("Enter shift key  :   "))
                encryption(st, shift)
            case 2:
                st2 = input("Enter encrypted text   :   ")
                shift2 = int(input("Enter shift key  :   "))
                decryption(st2, shift2)
            case 3:
                n = 0
            case _:
                print("Invalid Number\n")
