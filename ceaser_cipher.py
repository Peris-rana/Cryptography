def encrypt(text, key):
    cipher = ""
    for i in text:
        if i == " ":
            cipher = cipher + i
        elif i.isupper():
            cipher = cipher + chr((ord(i) + key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(i) + key - 97) % 26 + 97)
    return cipher


text_1 = input("Enter string: ")
key_1 = int(input("Enter shift number: "))
print("Original string: ", text_1)
print("After encryption: ", encrypt(text_1, key_1))


def decrypt(word, value):
    cipher_2 = ''
    for j in word:
        if j == ' ':
            cipher_2 = cipher_2 + j
        elif j.isupper():
            cipher_2 = cipher_2 + chr((ord(j) - value - 65) % 26 + 65)
        else:
            cipher_2 = cipher_2 + chr((ord(j) - value - 97) % 26 + 97)

    return cipher_2


text_2 = input("Enter string: ")
key_2 = int(input("Enter shift number: "))
print("Encrypted string: ", text_2)
print("After decryption: ", decrypt(text_2, key_2))
