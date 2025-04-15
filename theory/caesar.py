import argparse
from modes import Mode

# Constants
ALPHABET_LOWERCASE = [chr(ord('a') + i) for i in range(26)]

# Caesar cipher function
def caesar_cypher(alphabet: list[str], text: str, shift: int, mode: Mode) -> str:
    """
    Encrypts or decrypts the input text using the Caesar cipher algorithm.
    """
    # Performance improvements
    alphabet_dict = {char: i for i, char in enumerate(alphabet)}

    # Caesar cipher logic
    shifted = []
    for char in text:
        char_lower = char.lower()
        is_upper = char.isupper()
        if char_lower in alphabet_dict:
            index = alphabet_dict[char_lower]
            shifted_index = (index + (shift if mode == Mode.ENCRYPT.value else -shift)) % len(alphabet)
            shifted_char = alphabet[shifted_index]
            shifted.append(shifted_char if not is_upper else shifted_char.upper())
        else:
            print(f"Warning: '{char}' is not in the alphabet and will be skipped.")
            shifted.append(char)
    return ''.join(shifted)

# Define arguments for script usage
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Caesar Cipher")
    parser.add_argument(
        "-s", "--shift", type=int, required=True, help="shift value for the cipher"
    )
    parser.add_argument(
        "-m", "--mode", choices=[Mode.ENCRYPT.value, Mode.DECRYPT.value], required=True, help="mode of operation"
    )
    parser.add_argument(
        "-t", "--text", type=str, required=True, help="text to be encrypted/decrypted"
    )
    return parser.parse_args()

if __name__ == "__main__":
    # Args management
    args = parse_args()

    # Caesar cipher implementation
    result = caesar_cypher(ALPHABET_LOWERCASE, args.text, args.shift, args.mode)

    # Print the result
    print(f"Result: {result}")
