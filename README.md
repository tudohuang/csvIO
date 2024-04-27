# User Management System

This Python module provides basic functionalities for user registration, login, and password management. All passwords are encrypted using the SHA-256 algorithm to enhance security. The main features include user registration, user login, password encryption, and retrieval of encrypted passwords.

## Features

- **Password Encryption**: Encrypts passwords using the SHA-256 algorithm.
- **User Registration**: Allows new users to register. Registration fails if the username already exists.
- **User Login**: Verifies if the username and password are a match.
- **Password Retrieval**: Provides a username and retrieves the corresponding encrypted password.

## Usage

1. **Password Encryption**:
   ```python
   encrypted_password = crypto("your_password")
   ```

2. **User Registration**:
   ```python
   success = register("path_to_your_csv.csv", "username", "password")
   ```

3. **User Login**:
   ```python
   is_logged_in = login("path_to_your_csv.csv", "username", "password")
   ```

4. **Password Retrieval**:
   ```python
   password = get_password("path_to_your_csv.csv", "username")
   ```

## Installation Requirements

This module requires Python 3.6 or higher. External libraries used include:
- `csv`: For reading and writing CSV files.
- `hashlib`: For SHA-256 password encryption.
- `os`: To check if files exist.
