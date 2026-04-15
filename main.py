# ENIGMA MACHINE PROJECT

"""
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
"""

# Clean input


def clean_text(text):  # (text) in basicest words means the string of characters that the user inputs. This function is designed to clean that input by removing any unwanted spaces. The .strip() method is used to remove leading and trailing spaces from the input text, ensuring that the message is processed without extra spaces at the beginning or end. However, it keeps internal spaces intact, allowing for proper formatting of sentences and phrases.
    # this removes leading and trailing spaces, but keeps internal spaces intact by default. If you want to remove all spaces, you can use text.replace(" ", "") instead.
    return text.strip()

# Format output nicely

# parameter means the actual content that you want to display to the user. The function formats the output by printing a header with the label, followed by the message itself, and then a footer to visually separate it from other outputs., and the string means the actual content that you want to display to the user. The function formats the output by printing a header with the label, followed by the message itself, and then a footer to visually separate it from other outputs.


def format_output(label, message):  # (label, message) are the parameters that the function takes. The label is a string that describes the type of message being displayed (e.g., "Encrypted Message" or "Decrypted Message"), while the message is the actual content that you want to display to the user. The function formats the output by printing a header with the label, followed by the message itself, and then a footer to visually separate it from other outputs.
    # this is the header that displays the label (e.g., "Encrypted Message" or "Decrypted Message") in a visually distinct way. The underscores create a border around the label to make it stand out.
    print(f"\n___ {label} ___")
    # this is the actual content of the message that you want to display to the user. It will be printed below the header, allowing the user to easily see the result of their encryption or decryption.
    print(message)
    # this is the footer that visually separates the output from other outputs. It creates a line of underscores to indicate the end of the current message, making it easier for the user to distinguish between different outputs when they are displayed in sequence.
    print("_______________\n")

# Keyword Cipher Encryption


def keyword_encrypt(message_list, keyword):  # (message_list, keyword) are the parameters that the function takes. The message_list is a list of characters that represents the message to be encrypted, while the keyword is a string that will be used to determine how each letter in the message should be shifted. The function processes each character in the message_list, applying a shift based on the corresponding character in the keyword, and returns the resulting encrypted message as a string.
    if not keyword:
        raise ValueError("Keyword cannot be empty")
# we didn't use list here because in simple words the keyword is a string that will be used to determine how each letter in the message should be shifted. The function processes each character in the message_list, applying a shift based on the corresponding character in the keyword, and returns the resulting encrypted message as a string. Since we are only using the keyword to determine the shift for each letter, we can work with it as a string without needing to convert it into a list. The function will access individual characters of the keyword using indexing, which works directly with strings in Python.
    result = ""  # this variable will be used to build the encrypted message as the function processes each character in the message_list. It starts as an empty string and characters will be added to it one by one as they are encrypted.
    keyword = keyword.lower()
    key_index = 0

    for char in message_list:
        if char.isalpha():
            # ord() function returns the Unicode code point (integer value) of a given single character.
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')

            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)

            result += new_char
            key_index += 1
        else:
            result += char

    return result

# Keyword Cipher Decryption


def keyword_decrypt(message_list, keyword):
    if not keyword:
        raise ValueError("Keyword cannot be empty")

    result = ""
    keyword = keyword.lower()
    key_index = 0

    for char in message_list:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')

            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)

            result += new_char
            key_index += 1
        else:
            result += char

    return result

# Reverse Cipher


def reverse_cipher(message_list):
    # This line takes the message_list, reverses it using slicing with a step of -1 (message_list[::-1]), and then joins the reversed list of characters back into a single string using the join() method. The result is the original message reversed, which is the output of the reverse cipher.
    return "".join(message_list[::-1])


# Store history
history = []

#  NEW: Describe ciphers


def describe_ciphers():
    print("\n___ CIPHER DESCRIPTIONS ___")
    print("Keyword Cipher:")
    print("- Shifts each letter based on a repeating keyword.")
    print("- Example: 'A' with key 'B' becomes 'B'.")
    print()
    print("Reverse Cipher:")
    print("- Simply reverses the message.")
    print("- Example: 'hello' → 'olleh'")
    print("___________________________\n")

#  UPDATED TEST FUNCTION


def test_cipher():
    print("\n___ RUNNING TESTS ___")

    # Test 1: Keyword Cipher
    original1 = "hello world"
    keyword = "key"

    encrypted1 = keyword_encrypt(list(original1), keyword)
    decrypted1 = keyword_decrypt(list(encrypted1), keyword)

    if original1 == decrypted1:
        print(" Keyword Cipher Test PASSED")
    else:
        print(" Keyword Cipher Test FAILED")
        print(f"Expected: {original1}")
        print(f"Got:      {decrypted1}")

    # Test 2: Reverse Cipher
    original2 = "python is fun"

    encrypted2 = reverse_cipher(list(original2))
    decrypted2 = reverse_cipher(list(encrypted2))

    if original2 == decrypted2:
        print(" Reverse Cipher Test PASSED")
    else:
        print(" Reverse Cipher Test FAILED")
        print(f"Expected: {original2}")
        print(f"Got:      {decrypted2}")

    print("______________________\n")


# MAIN PROGRAM LOOP
while True:
    print("\n___ ENIGMA MACHINE ___")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. View History")
    print("4. Run Test")
    print("5. Describe Ciphers")  # NEW OPTION
    print("6. Quit")

    choice = input("Enter choice: ").strip()

    # ENCRYPT
    if choice == "1":
        print("\nChoose cipher:")
        print("1. Keyword")
        print("2. Reverse")

        cipher_choice = input("Enter option: ").strip()

        try:
            print("Enter your message below (letters, numbers, symbols allowed):")
            message = clean_text(input("Enter MESSAGE: "))
            message_list = list(message)

            if cipher_choice == "1":
                print("Keyword Cipher shifts letters based on a repeating keyword.")
                keyword = input("Enter keyword: ").strip()
                print(" Encrypting using Keyword Cipher...")
                result = keyword_encrypt(message_list, keyword)

            elif cipher_choice == "2":
                print(" Reversing message...")
                result = reverse_cipher(message_list)

            else:
                print("Invalid option")
                continue

            format_output("Encrypted Message", result)
            print(f"Processed {len(message)} characters.")
            history.append(("Encrypt", message, result))

        except ValueError as e:
            print(f" Input Error: {e}")
        except Exception:
            print(" Unexpected error occurred. Please try again.")

    # DECRYPT
    elif choice == "2":
        print("\nChoose cipher:")
        print("1. Keyword")
        print("2. Reverse")

        cipher_choice = input("Enter option: ").strip()

        try:
            print("Enter your message below (letters, numbers, symbols allowed):")
            message = clean_text(input("Enter MESSAGE: "))
            message_list = list(message)

            if cipher_choice == "1":
                print(" Decrypting using Keyword Cipher...")
                keyword = input("Enter keyword: ").strip()
                result = keyword_decrypt(message_list, keyword)

            elif cipher_choice == "2":
                print(" Reversing message...")
                result = reverse_cipher(message_list)

            else:
                print("Invalid option")
                continue

            format_output("Decrypted Message", result)
            print(f"Processed {len(message)} characters.")
            history.append(("Decrypt", message, result))

        except ValueError as e:
            print(f" Input Error: {e}")
        except Exception:
            print(" Unexpected error occurred. Please try again.")

    # HISTORY
    elif choice == "3":
        print("\n___ HISTORY ___")
        if not history:
            print("No history yet.")
        else:
            for i, (action, original, result) in enumerate(history, start=1):
                print(f"{i}. {action}")
                print(f"   Original : {original}")
                print(f"   Result   : {result}")
                print("-" * 30)

    # TEST
    elif choice == "4":
        test_cipher()

    #  NEW: DESCRIBE
    elif choice == "5":
        describe_ciphers()

    # QUIT
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
