
# ENIGMA MACHINE PROJECT
'''
PSEUDOCODE
1. Display menu (encrypt, decrypt, quit, history, test)
2. Ask user for choice
3. If encrypt:
      ask for message
      clean message (strip spaces)
      ask for cipher type (caesar, reverse, keyword)
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


def clean_text(text):  # Clean text by removing leading/trailing spaces
    return text.strip()
