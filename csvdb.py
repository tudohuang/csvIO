import csv
import hashlib
import os

def crypto(text):
    """
    Encrypt the password using SHA-256.

    Args:
    text (str): The password to encrypt.
    
    Returns:
    str: The encrypted password.
    """
    try:
        text_bytes = text.encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(text_bytes)
        return sha256_hash.hexdigest()
    except Exception:
        return None

def register(csv_route, username, password):
    """
    Register a new user with encrypted password.

    Args:
    csv_route (str): Path to the CSV database.
    username (str): User's username.
    password (str): User's password.
    
    Returns:
    bool: True if registration successful, False otherwise.
    """
    try:
        file_exists = os.path.isfile(csv_route)
        if file_exists:
            with open(csv_route, 'r', newline='', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    cryusername = crypto(username)
                    if row['username'] == cryusername:
                        return False
        with open(csv_route, 'a', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['username', 'password']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)        
            if not file_exists:
                writer.writeheader()
            encrypted_password = crypto(password)
            encrypted_username = crypto(username)
            if encrypted_password is None:
                return False
            writer.writerow({'username': encrypted_username, 'password': encrypted_password})
        return True
    except Exception:
        return False

def get_password(csv_route, username):
    """
    Retrieve the hashed password for a username.

    Args:
    csv_route (str): Path to the CSV file.
    username (str): Username to search for.

    Returns:
    str or bool: Hashed password if found, False otherwise.
    """
    try:
        with open(csv_route, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            encrypted_username = crypto(username)
            for row in reader:
                if row['username'] == encrypted_username:
                    return row['password']
        return False
    except Exception:
        return False

def login(csv_route, username, password):
    """
    Verify user login credentials.

    Args:
    csv_route (str): Path to the CSV file.
    username (str): Username to verify.
    password (str): Password to verify.
    
    Returns:
    bool: True if credentials match, False otherwise.
    """
    try:
        real_password = get_password(csv_route, username)
        if real_password:
            return crypto(password) == real_password
        return False
    except Exception:
        return False
