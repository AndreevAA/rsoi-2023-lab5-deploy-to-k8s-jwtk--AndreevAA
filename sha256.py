from passlib.hash import pbkdf2_sha256

def encode_password(password):
    # Генерация хэша пароля с помощью PBKDF2-SHA256
    hash = pbkdf2_sha256.hash(password, rounds=390000)
    return hash

# Пример использования
password = input()
encoded_password = encode_password(password)
print("Закодированный пароль:", encoded_password)
