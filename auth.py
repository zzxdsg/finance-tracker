import hashlib

# User data file
USERS_FILE = 'users.txt'

def hash_password(password):
    """对密码进行加密处理。"""
    return hashlib.sha256(password.encode()).hexdigest()

def username_exists(username):
    """检查用户名是否已经存在。"""
    try:
        with open(USERS_FILE, 'r') as file:
            for line in file:
                stored_username, _, _ = line.strip().split(',')
                if stored_username == username:
                    return True
    except FileNotFoundError:
        pass  # 如果文件不存在，视为没有用户名冲突
    return False

def register(username, password):
    """注册新用户并将信息保存到文件。"""
    if username_exists(username):
        return False, "Username already exists, please choose another one!"

    try:
        with open(USERS_FILE, 'a+') as file:
            file.write(f"{username},{hash_password(password)}\n")
        return True, "Registration successful!"
    except Exception as e:
        return False, f"Registration failed: {e}"

def login(username, password):
    """用户登录，验证用户名和密码。"""
    try:
        with open(USERS_FILE, 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')
                if stored_username == username and stored_password == hash_password(password):
                    return True, "Login successful!"
    except FileNotFoundError:
        return False, "Login failed: User data file not found."
    except Exception as e:
        return False, f"Login failed: {e}"

    return False, "Username or password incorrect!"


# Test code
if __name__ == "__main__":
    while True:
        choice = input("1. Login\n2. Register\nPlease choose (1/2): ")
        if choice == '1':
            usr = input("Username: ").strip()
            pwd = input("Password: ").strip()
            if not usr or not pwd:
                print("Username and password cannot be empty.")
                continue
            success, message = login(usr, pwd)
            print(message)
        elif choice == '2':
            usr = input("Username: ").strip()
            pwd = input("Password: ").strip()
            contact = input("Contact Information: ").strip()
            if not usr or not pwd:
                print("Username and password cannot be empty.")
                continue
            success, message = register(usr, pwd, contact)
            print(message)
