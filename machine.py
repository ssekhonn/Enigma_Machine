# =============================
# TRUE ENIGMA MACHINE (FULL VERSION)
# =============================

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


# -----------------------------
# MACHINE FACTORY (RESET STATE)
# -----------------------------
def create_machine():
    return {
        "rotors": [3, 1, 7],
        "step": 0
    }


plugboard = {
    "a": "m", "m": "a",
    "t": "k", "k": "t",
    "s": "x", "x": "s"
}


history = []


# -----------------------------
# CORE FUNCTIONS
# -----------------------------
def swap_plugboard(c):
    return plugboard.get(c, c)


def rotate_rotors(machine):
    machine["step"] += 1

    machine["rotors"][2] = (machine["rotors"][2] + 1) % 26

    if machine["step"] % 2 == 0:
        machine["rotors"][1] += 1
    if machine["step"] % 5 == 0:
        machine["rotors"][0] += 1


def enigma(text, keyword, mode="encrypt"):
    machine = create_machine()

    result = ""
    keyword = keyword.lower()
    key_index = 0

    for char in text:

        if char.isalpha():

            c = char.lower()

            # plugboard in
            c = swap_plugboard(c)

            # keyword shift
            k = ord(keyword[key_index % len(keyword)]) - ord('a')

            r1, r2, r3 = machine["rotors"]
            shift = (k + r1 + r2 + r3) % 26

            idx = ALPHABET.index(c)

            if mode == "encrypt":
                idx = (idx + shift) % 26
            else:
                idx = (idx - shift) % 26

            new_char = ALPHABET[idx]

            # plugboard out
            new_char = swap_plugboard(new_char)

            if char.isupper():
                new_char = new_char.upper()

            result += new_char
            key_index += 1

            rotate_rotors(machine)

        else:
            result += char

    return result


# -----------------------------
# FEATURES
# -----------------------------
def describe():
    print("\n--- ENIGMA MACHINE ---")
    print("Rotor-based encryption system")
    print("Plugboard swaps letters")
    print("Keyword influences shifting")
    print("Rotors change every character")
    print("-----------------------\n")


def test():
    print("\n--- TESTING MACHINE ---")

    msg = "hello world"
    key = "key"

    enc = enigma(msg, key, "encrypt")
    dec = enigma(enc, key, "decrypt")

    if msg == dec:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        print("Expected:", msg)
        print("Got:", dec)

    print("-----------------------\n")


def show_history():
    print("\n--- HISTORY ---")
    if not history:
        print("No history")
    else:
        for i, h in enumerate(history, 1):
            print(f"{i}. {h['type']}")
            print("Input :", h["input"])
            print("Output:", h["output"])
            print("----------------")


# -----------------------------
# MAIN MENU
# -----------------------------
while True:
    print("\n=== ENIGMA MACHINE ===")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. History")
    print("4. Test")
    print("5. Describe")
    print("6. Quit")

    choice = input("> ").strip()

    if choice in ["1", "2"]:

        msg = input("Message: ")
        key = input("Keyword: ")

        if choice == "1":
            result = enigma(msg, key, "encrypt")
            print("\nENCRYPTED:", result)
            action = "ENCRYPT"
        else:
            result = enigma(msg, key, "decrypt")
            print("\nDECRYPTED:", result)
            action = "DECRYPT"

        history.append({
            "type": action,
            "input": msg,
            "output": result
        })

    elif choice == "3":
        show_history()

    elif choice == "4":
        test()

    elif choice == "5":
        describe()

    elif choice == "6":
        print("Shutting down Enigma...")
        break

    else:
        print("Invalid choice")
