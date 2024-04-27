# 用戶管理系統

## 功能說明

- **密碼加密**：使用 SHA-256 演算法對密碼進行加密。
- **用戶註冊**：允許新用戶註冊。若用戶名已存在，則註冊失敗。
- **用戶登入**：驗證用戶名與密碼是否匹配。
- **查詢密碼**：提供一個用戶名，查詢並返回對應的加密密碼。

## 使用方法

1. **密碼加密**：
   ```python
   encrypted_password = crypto("your_password")
   ```

2. **用戶註冊**：
   ```python
   success = register("path_to_your_csv.csv", "username", "password")
   ```

3. **用戶登入**：
   ```python
   is_logged_in = login("path_to_your_csv.csv", "username", "password")
   ```

4. **查詢密碼**：
   ```python
   password = get_password("path_to_your_csv.csv", "username")
   ```

## 安裝需求

本模組需要 Python 3.6 或更高版本。依賴的外部庫包括：
- `csv`：用於讀取和寫入 CSV 文件。
- `hashlib`：用於進行 SHA-256 密碼加密。
- `os`：用於檢查文件是否存在。
