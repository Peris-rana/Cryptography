# Cryptography

## Caeser Cipher

A **Caeser cipher** is a simple method of encoding messages.This technique was first used by Julius Caeser to communicate with his officers.It is a kind of replacement cipher , where all the letter of the plain text are replaced by another letter.

**Plaintext** - simple messege written by the user.  
**Ciphertext** - encrypted messege after applying the technique.

when encrypting

```text
Plain :  hello
Key   :  3
Cipher:  khoor
```

when decrypting

```text
Cipher : khoor
Key    : 3
Plain  : hello
```

The cipher value depends upon the **key.**
<br>
<br>

## Formula<br>

<br>

### Encryption

**E = (x + key) mod 26**
<br>

### Decryption

**D = (x - key) mod 26**  
 [CLick here](https://github.com/Peris-rana/Cryptography/blob/main/caeser_cipher.py) to view the program.<br><br>

## References

[Caesar cipher on Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
<br>
<br>
<br>

## Playfair Cipher

**Playfair Cipher** uses substitution tecnhnique and is a multiple letter encryption cipher.It is used to encrypt or encode a message.<br>
An initial **5X5** matrix is created.The plain text encryption key is made out of the matrix alphabetic character but the letters should not be repeated.<br>

### Algorithm

1. Convert plain text into the pair of two letters.
2. Generate a cipher key matrix.
3. Encrypt plain text using the cipher key matrix and get the cipher text.
   <br>
   <br>

### Convert plain text into the pair of two letters.

1. While splitting text into pairs, if the letters are same in a pair then insert filler x.

2. At the end if only one letter is left it has no pair we can insert our filler x.

3. Remove Whitespaces from the string as well as special characters apart from 25 alphabets.
   <br>
   <br>

### Generate a cipher key matrix

The matrix should be 5X5.
Each of the 25 alphabets must be unique and one letter of the alphabet (usually J) is omitted from the table (as the table can hold only 25 alphabets).If the plaintext contains J, then it is replaced by I.<br>

1. If our key has repeating letters omit them.
2. Fill the matrix without repeating the letter.
3. Fill the remaining places with unused alphabets.
   <br>
   <br>

### Encrypt plaintext using Cipher Key Matrix and get ciphertext.

### Rules

1. If both letters are not in same column and not in same row then draw a imaginary rectangle shape and take letters on the horizontal opposite corner of the rectangle.
2. If both the letters are in the same column: Take the letter below each one (going back to the top if at the bottom).
3. If both the letters are in the same row: Take the letter to the right of each one (going back to the leftmost if at the rightmost position).
   <br>
   <br>

[Click here](https://github.com/Peris-rana/Cryptography/blob/main/playfair_cipher.cpp) to view the program.
## References

[Playfair Cipher Encryption Algorithm](https://dev.to/karanmunjani/what-is-playfair-cipher-encryption-algorithm-4npk)
