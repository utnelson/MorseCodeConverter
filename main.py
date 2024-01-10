

morse_alphabet = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                  "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                  "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                  "y": "-.--", "z": "--.."}
morse_reversed_alphabet = {value: key for key, value in morse_alphabet.items()}

input_string = input("Input String: ").lower()
input_direction = int(input("Enter Translation Mode (1=ToMorseCode/2=ToPlainText: "))

# To morse code
if input_direction == 1:
    for char in input_string:
        if char in morse_alphabet:
            print(morse_alphabet[char], end=' ')
        else:
            print(end=' ')

# To plain text
elif input_direction == 2:
    morse_words = input_string.split("  ")
    for morse_word in morse_words:
        morse_chars = morse_word.split(" ")
        for morse_char in morse_chars:
            if morse_char in morse_reversed_alphabet:
                print(morse_reversed_alphabet[morse_char], end='')
        print(end=" ")

















