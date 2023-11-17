import mysql.connector
from mysql.connector import Error

def create_db_connection():
    """创建到MySQL数据库的连接"""
    try:
        connection = mysql.connector.connect(
            host='localhost',  # 或你的服务器地址
            user='root',
            password='Zzx2004515',
            database='finance_tracker'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


import hashlib

def register_user(username, password, contact_info):
    """注册新用户"""
    conn = create_db_connection()
    if conn is not None:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, contact_info) VALUES (%s, %s, %s)", (username, hashed_password, contact_info))
            conn.commit()
            return True, "注册成功！"
        except Error as e:
            return False, f"注册失败: {e}"
        finally:
            cursor.close()
            conn.close()
    else:
        return False, "数据库连接失败"





def login_user(username, password):
    """用户登录"""
    conn = create_db_connection()
    if conn is not None:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
            if cursor.fetchone():
                return True, "登录成功！"
            else:
                return False, "用户名或密码错误。"
        except Error as e:
            return False, f"登录失败: {e}"
        finally:
            cursor.close()
            conn.close()
    else:
        return False, "数据库连接失败"

