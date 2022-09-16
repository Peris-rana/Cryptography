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
The program is written [here](https://github.com/Peris-rana/Cryptography/blob/main/ceaser_cipher.py) please have a look.<br><br>

## References

[Caesar cipher on Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
