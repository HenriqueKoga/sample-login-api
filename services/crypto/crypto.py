import bcrypt


def create_bcrypt_hash(password):
    password_bytes = password.encode()
    salt = bcrypt.gensalt(14)
    password_hash_bytes = bcrypt.hashpw(password_bytes, salt)
    return password_hash_bytes.decode()


def verify_password(password, hash_from_database):
    password_bytes = password.encode()
    hash_bytes = hash_from_database.encode()
    return bcrypt.checkpw(password_bytes, hash_bytes)
