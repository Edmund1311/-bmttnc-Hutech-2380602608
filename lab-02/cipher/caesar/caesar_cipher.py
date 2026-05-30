from cipher.caesar.alphabet import ALPHABET   

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    # Đổi tên thành encrypt_text và thêm tham số key
    def encrypt_text(self, plaintext, key):
        cipher_text = ""
        for char in plaintext:
            if char.upper() in ALPHABET:
                # Sử dụng key được truyền từ API vào thay vì self.shift
                index = (ALPHABET.index(char.upper()) + key) % len(ALPHABET)
                cipher_text += ALPHABET[index]
            else:
                cipher_text += char
        return cipher_text

    # Đổi tên thành decrypt_text và thêm tham số key
    def decrypt_text(self, ciphertext, key):
        plain_text = ""
        for char in ciphertext:
            if char.upper() in ALPHABET:
                # Sử dụng key được truyền từ API vào
                index = (ALPHABET.index(char.upper()) - key) % len(ALPHABET)
                plain_text += ALPHABET[index]
            else:
                plain_text += char
        return plain_text