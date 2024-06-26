# User Management System
[![Chinese Version](https://img.shields.io/badge/-中文版-blue)](https://github.com/tudohuang/csvIO/blob/main/README-ch.md)
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

This module requires Python 3.6 or higher. Using the following command to get the module
```fix
pip install git+https://github.com/tudohuang/csvIO.git
```
```python
import csvIO
encrypted_password = csvIO.crypto("your_password")
success = csvIO.register("path_to_your_csv.csv", "username", "password")
is_logged_in = csvIO.login("path_to_your_csv.csv", "username", "password")
password = csvIO.get_password("path_to_your_csv.csv", "username")
```
