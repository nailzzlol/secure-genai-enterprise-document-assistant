from cryptography.fernet import Fernet

# Create key only once
try:

    with open(
        "secret.key",
        "rb"
    ) as f:

        key = f.read()

except:

    key = Fernet.generate_key()

    with open(
        "secret.key",
        "wb"
    ) as f:

        f.write(key)

cipher = Fernet(key)


def encrypt_file(
    data
):

    return cipher.encrypt(
        data
    )


def decrypt_file(
    data
):

    return cipher.decrypt(
        data
    )