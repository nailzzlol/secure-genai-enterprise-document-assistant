import hashlib

USERS = {
    "admin":
    hashlib.sha256(
        "admin123".encode()
    ).hexdigest(),

    "employee":
    hashlib.sha256(
        "emp123".encode()
    ).hexdigest()
}

failed_attempts = {}

def login(
    username,
    password
):

    hashed = hashlib.sha256(
        password.encode()
    ).hexdigest()

    if (
        username in USERS
        and USERS[username]
        == hashed
    ):

        failed_attempts[
            username
        ] = 0

        return True

    failed_attempts[
        username
    ] = failed_attempts.get(
        username,
        0
    ) + 1

    return False