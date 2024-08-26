import random as ran

# Ask the user whether they want to encrypt or decrypt
choice = int(input("Do you want to Encrypt [1] or Decrypt [2]? Please input number: "))

if choice == 1:
    # Encryption
    inp = input("Input text to encrypt: ")
    rnd = ran.randint(1, 100)  # Generate a random encryption key

    # Convert input text to bytes
    byte_data = inp.encode('utf-8')

    # Prepare for encryption
    length = len(byte_data)
    lst = []

    # Encrypt each byte
    for l in range(length):
        enc = byte_data[l] + rnd
        lst.append(enc)

    # Convert encrypted values to characters
    letters = [chr(value) for value in lst]

    # Display encryption key and result
    print("Your encryption key is:", rnd)
    print(lst)
    print("Encrypted characters:", ''.join(letters))

elif choice == 2:
    # Decryption
    encoded_values_str = input("Please input encoded values separated by commas: ")
    rnd = int(input("Input encryption key: "))  # Get the encryption key used in encoding

    # Convert input string to a list of integers
    encoded_values = [int(value.strip()) for value in encoded_values_str.split(',')]

    # Decrypt the values
    decrypted_values = [value - rnd for value in encoded_values]

    # Convert decrypted ASCII values to characters
    letters = [chr(value) for value in decrypted_values]

    # Display results
    print("Decrypted ASCII values:", decrypted_values)
    print("Characters:", ''.join(letters))

else:
    print("Invalid choice. Please enter 1 for Encryption or 2 for Decryption.")
