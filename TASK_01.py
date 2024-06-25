def caesar_cipher(text, shift, mode):

  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''
  for char in text:
    if char.isalpha():
      new_index = (alphabet.find(char) + shift) % len(alphabet)
      result += alphabet[new_index]
    else:
      result += char
  return result

def main():
  while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
      mode = 'encrypt'
    elif choice == '2':
      mode = 'decrypt'
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")
      continue

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value ((-25)-25): "))

    if shift < -25 or shift > 25:
      print("Shift value must be between (-25) and 25.")
      continue

    result = caesar_cipher(text, shift, mode)
    print(f"{'Encrypted' if mode == 'encrypt' else 'Decrypted'} message: {result}")

if __name__ == "__main__":
  main()
