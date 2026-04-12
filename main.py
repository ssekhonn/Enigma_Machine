
# ENIGMA MACHINE PROJECT
'''
PSEUDOCODE
1. Display menu (encrypt, decrypt, quit, history, test)
2. Ask user for choice
3. If encrypt:
      ask for message
      clean message (strip spaces)
      ask for cipher type (reverse, keyword)
      apply encryption
4. If decrypt:
      same process but reverse
5. Store result in history list
6. Allow user to view history
7. Allow user to run test function
8. Repeat program using loop
9. Handle invalid input using try/except
10. Add secret feature (admin or random shift)

'''
# ENIGMA MACHINE PROJECT

import random


def clean_text(text):
    return text.strip()


# Keyword Cipher Encryption
def keyword_encrypt(text, keyword):
    result = ""
    keyword = keyword.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            new_char = chr((ord(char.lower()) - ord('a') + shift) %
                           26 + ord('a'))
            result += new_char
            key_index += 1
        else:
            result += char

    return result


# Keyword Cipher Decryption
def keyword_decrypt(text, keyword):
    result = ""
    keyword = keyword.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            new_char = chr((ord(char.lower()) - ord('a') - shift) %
                           26 + ord('a'))
            result += new_char
            key_index += 1
        else:
            result += char

    return result


# Reverse Cipher
def reverse_cipher(text):
    return text[::-1]


# Store history
history = []


# FIXED test function
def test_cipher():
    original = "hello"
    keyword = "key"

    encrypted = keyword_encrypt(original, keyword)
    decrypted = keyword_decrypt(encrypted, keyword)

    if original == decrypted:
        print("Test passed!")
    else:
        print("Test failed!")


while True:
    print("\nENIGMA MACHINE")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. View History")
    print("4. Run Test")
    print("5. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        message = clean_text(input("Enter MESSAGE: "))

        # Secret feature
        if message == "admin":
            print("Access granted")
            continue

        print("Choose cipher:")
        print("1. Keyword")
        print("2. Reverse")

        cipher_choice = input("Enter option: ")

        if cipher_choice == "1":
            keyword = input("Enter keyword: ")
            result = keyword_encrypt(message, keyword)

        elif cipher_choice == "2":
            result = reverse_cipher(message)

        else:
            print("Invalid option")
            continue

        print("Encrypted message:", result)
        history.append(("Encrypt", message, result))

    elif choice == "2":
        message = clean_text(input("Enter message: "))

        print("Choose cipher:")
        print("1. Keyword")
        print("2. Reverse")

        cipher_choice = input("Enter option: ")

        if cipher_choice == "1":
            keyword = input("Enter keyword: ")
            result = keyword_decrypt(message, keyword)

        elif cipher_choice == "2":
            result = reverse_cipher(message)

        else:
            print("Invalid option")
            continue

        print("Decrypted message:", result)
        history.append(("Decrypt", message, result))

    elif choice == "3":
        print("\nHISTORY")
        for item in history:
            action, original, result = item
            print(f"{action}: {original} → {result}")

    elif choice == "4":
        test_cipher()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
