# ENIGMA MACHINE PROJECT

'''
PSEUDOCODE
1. Show menu (encrypt, decrypt, history, test, quit)
2. Ask user for input
3. Clean message (strip spaces)
4. Convert message into a LIST
5. Choose cipher (keyword or reverse)
6. Call function with LIST parameter
7. Store results in history
8. Allow repeated use with loop
9. Handle errors using try/except
10. Display clean formatted output
'''

import random


# Clean input
def clean_text(text):
    return text.strip()


# Format output nicely
def format_output(label, message):
    print(f"\n___{label}___")
    print(message)
    print("_________\n")


# Keyword Cipher Encryption (uses LIST)
def keyword_encrypt(message_list, keyword):
    result = ""
    keyword = keyword.lower()
    key_index = 0

    for char in message_list:
        if char.isalpha():  # condition
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            new_char = chr((ord(char.lower()) - ord('a') + shift) %
                           26 + ord('a'))
            result += new_char
            key_index += 1
        else:
            result += char

    return result


# Keyword Cipher Decryption (uses LIST)
def keyword_decrypt(message_list, keyword):
    result = ""
    keyword = keyword.lower()
    key_index = 0

    for char in message_list:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            new_char = chr((ord(char.lower()) - ord('a') - shift) %
                           26 + ord('a'))
            result += new_char
            key_index += 1
        else:
            result += char

    return result


# Reverse Cipher (also uses LIST for consistency)
def reverse_cipher(message_list):
    return "".join(message_list[::-1])


# Store history using LIST of TUPLES (data structure mastery)
history = []


# Test function
def test_cipher():
    original = "hello world"
    keyword = "key"

    message_list = list(original)

    encrypted = keyword_encrypt(message_list, keyword)
    decrypted = keyword_decrypt(list(encrypted), keyword)

    if original == decrypted:
        print("\nTest passed! Cipher works correctly.\n")
    else:
        print("\nTest failed.\n")


# MAIN PROGRAM LOOP
while True:
    print("\n ___ ENIGMA MACHINE ___ ")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. View History")
    print("4. Run Test")
    print("5. Quit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        message = clean_text(input("Enter MESSAGE: "))

        # Secret feature
        if message.lower() == "admin":
            print("Access granted")
            continue

        message_list = list(message)

        print("\nChoose cipher:")
        print("1. Keyword")
        print("2. Reverse")

        cipher_choice = input("Enter option: ").strip()

        try:
            if cipher_choice == "1":
                keyword = input("Enter keyword: ").strip()
                result = keyword_encrypt(message_list, keyword)

            elif cipher_choice == "2":
                result = reverse_cipher(message_list)

            else:
                print("Invalid option")
                continue

            format_output("Encrypted Message", result)
            history.append(("Encrypt", message, result))

        except:
            print("Error occurred during encryption")

    elif choice == "2":
        message = clean_text(input("Enter message: "))
        message_list = list(message)

        print("\nChoose cipher:")
        print("1. Keyword")
        print("2. Reverse")

        cipher_choice = input("Enter option: ").strip()

        try:
            if cipher_choice == "1":
                keyword = input("Enter keyword: ").strip()
                result = keyword_decrypt(message_list, keyword)

            elif cipher_choice == "2":
                result = reverse_cipher(message_list)

            else:
                print("Invalid option")
                continue

            format_output("Decrypted Message", result)
            history.append(("Decrypt", message, result))

        except:
            print("Error occurred during decryption")

    elif choice == "3":
        print("\n___ HISTORY ___")
        if not history:
            print("No history yet.")
        else:
            for action, original, result in history:
                print(f"{action}: {original} → {result}")

    elif choice == "4":
        test_cipher()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
