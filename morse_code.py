# Coding Challenge 2
# Name:
# Student No:

# A Morse code encoder/decoder
"""path module for checking file existence"""
from os import path

MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"),
    ("..-.", "F"), ("--.", "G"), ("....", "H"), ("..", "I"), (".---", "J"),
    ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"), ("---", "O"),
    (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"),
    ("..-", "U"), ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"),
    ("--..", "Z"), (".-.-.-", "."), ("-----", "0"), (".----", "1"), ("..---", "2"),
    ("...--", "3"), ("....-", "4"), (".....", "5"), ("-....", "6"), ("--...", "7"),
    ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"), (".-...", "&"),
    ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"),
    ("-.-.--", "!")
)

def print_intro():
    """Intro function which displays welcome message and what the program does"""

    print("Welcome to Wolmorse")
    print("This program encodes and decodes Morse code.")


def get_input():
    """function to get the mode of operation, and the message to perform the operation on"""

    while True:
        mode = input('Would you like to encode (e) or decode (d) : ')
        if mode == 'e':
            message = input('What message would you like to encode : ')
            # message = message if message.isupper() else message.upper()
            break
        if mode == 'd':
            message = input('What message would you like to decode : ')
            break

        print('Invalid mode')

    return (mode, message)


def encode(message):
    """function which performs encoding of a message"""

    morse_words = message.split(' ')
    morse_string = []
    for morse_word in morse_words:
        morse_code = []
        for morse_char in morse_word:
            for morse_map in MORSE_CODE:
                if morse_char == morse_map[1]:
                    morse_code.append(morse_map[0])
        morse_string.append(' '.join(morse_code))

    encoded_str = '   '.join(morse_string)
    return encoded_str



def decode(message):
    """function which performs decoding of a message"""

    morse_words = message.split('   ')
    morse_string = []
    for word in morse_words:
        morse_chars = word.split(' ')
        morse_alpha = ''

        for morse_char in morse_chars:
            for morse_map in MORSE_CODE:
                if morse_char == morse_map[0]:
                    morse_alpha += morse_map[1]
        morse_string.append(morse_alpha)

    decoded_str = ' '.join(morse_string)
    return decoded_str


# ---------- Challenge Functions (Optional) ----------


def process_lines(filename, mode):
    """function which reads the lines of a file and performs an operation on it
    based on the mode the user inputs"""

    with open(filename) as input_file:
        messages = input_file.read().splitlines()

    if mode == 'e':
        result = list(map(encode, messages))

    elif mode == 'd':
        result = list(map(decode, messages))

    return result


def write_lines(lines):
    """function which writes to a file the result of an operation"""

    with open('results.txt', 'w') as output_file:
        output_file.writelines("%s\n" % line for line in lines)


def check_file_exists(filename):
    """function which checks the existence of a file in the currwnt directory"""

    return path.exists(filename)

def get_filename():
    """function to get file name alone, serves as a decomposed function of get_filename_input()"""

    while True:
        filename = input('Enter a filename : ')
        if check_file_exists(filename):
            break
        print('Invalid filename')

    return filename

def valid_mode_controller(mode):
    """function executed for a valid mode, needed inorder to reduce nested loop complexity
    and pep8 compliancy"""

    while True:
        action = input('Would you like to read from a file (f) for console (c) : ')
        if action == 'c':
            filename = None
            if mode == 'e':
                message = input('What message would you like to encode : ')
                message = message if message.isupper() else message.upper()
                break
            if mode == 'd':
                message = input('What message would you like to decode : ')
                break

        elif action == 'f':
            message = None
            while True:
                filename = input('Enter a filename : ')
                if check_file_exists(filename):
                    break
                print('Invalid filename')

            break

        else:
            print('Invalid action')

    return (message, filename)

def get_filename_input():
    """function which requests the mode of operation, an whether a user wishes to
    perform the operation on a console message or lines in a file, and the appropriate
    message entered or filename to read the messages"""

    while True:
        mode = input('Would you like to encode (e) or decode (d) : ')
        if mode in ('e', 'd'):
            (message, filename) = valid_mode_controller(mode)
            break

        print('Invalid mode')

    return (mode, message, filename)


def main_init():
    """driver function for required tasks"""
    while True:
        (mode, message) = get_input()
        if mode == 'e':
            result = encode(message)
            print(result)

        elif mode == 'd':
            result = decode(message)
            print(result)

        choice = input('Would you like to encode/decode another message? (y/n) : ')
        if choice in ('n', 'N'):
            break
        if choice in ('y', 'Y'):
            main_init()
        print('Invalid response')


def main():
    """driver function for required and additional tasks"""
    while True:
        (mode, message, filename) = get_filename_input()
        if filename is None:
            if mode == 'e':
                result = encode(message)
                print(result)

            elif mode == 'd':
                result = decode(message)
                print(result)

        if message is None:
            result = process_lines(filename, mode)
            write_lines(result)

        choice = input('Would you like to encode/decode another message? (y/n) : ')
        if choice in ('n', 'N'):
            return
        if choice in ('y', 'Y'):
            main()
        print('Invalid response')




# Program execution begins here
if __name__ == '__main__':
    main()
