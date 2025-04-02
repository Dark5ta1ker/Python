import pandas as pd
import hashlib
import re
from cryptography.fernet import Fernet

# Загрузка данных
file_path = "E:/Мои документы/Desktop/Уроки/Python/ИТИП/Laptop_price.csv" 
try:
    df = pd.read_csv(file_path)  # Читаем CSV-файл и загружаем его в DataFrame
except Exception as e:
    print(f"Ошибка загрузки файла: {e}")

# 1. Проверка CSV на уязвимости (CSV Injection)
# Опасные символы могут использоваться для атак в Excel и других программах
# Функция проверяет, начинаются ли значения в текстовых столбцах с этих символов
# Функция доработана с учетом требований - добавлена проверка на пробелы
def check_csv_injection(df):
    dangerous_chars = ('=', '+', '-', '@')
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].astype(str).apply(
            lambda x: x.startswith(dangerous_chars) or  
            x.lstrip().startswith(dangerous_chars)).any():
            print(f"Обнаружены потенциальные CSV-инъекции в столбце {col}!")
        else:
            print(f"Столбец {col} безопасен.")

check_csv_injection(df)

# 2. Фильтрация данных от SQL-инъекций и XSS-атак
# SQL-инъекции используются для взлома баз данных, а XSS – для атак на пользователей
# Функция заменяет опасные конструкции на строку '[BLOCKED]'
# Дописана проверка на xss-паттерны, также, в соответствии с заданием, добавлена проверка на SQL-комментарии
def clean_input(value):
    sql_keywords = ["SELECT", "DROP", "DELETE", "INSERT", "UPDATE", "ALTER", "UNION", "--"]  
    xss_patterns = [r'<script.*>,*></script>', r'javascript:.*', r'onerror=.*']  # XSS-скрипты

    for keyword in sql_keywords:
        if keyword.lower() in value.lower():
            return "[BLOCKED_SQL]"

    for pattern in xss_patterns:
        if re.search(pattern, value, re.IGNORECASE):
            return "[BLOCKED_XSS]"
    return value

df = df.map(lambda x: clean_input(str(x)) if isinstance(x, str) else x)
print("Фильтрация данных завершена.")

# 3. Хеширование столбца с ценами (SHA-256)
# Хеширование используется для защиты конфиденциальных данных, таких как пароли
# В данном случае мы хешируем цену ноутбука, чтобы скрыть оригинальные значения
def hash_price(price):
    return hashlib.sha256(str(price).encode()).hexdigest()

df['Price_hashed'] = df['Price'].apply(hash_price)
print("Столбец с хешированными ценами добавлен.")

# 4. Шифрование данных (например, цены ноутбуков)
# Шифрование позволяет скрыть данные, но при этом их можно расшифровать при наличии ключа
# Генерируем ключ и шифруем цену ноутбука
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_price(price):
    return cipher.encrypt(str(price).encode()).decode()

def decrypt_price(encrypted_price):
    return cipher.decrypt(encrypted_price.encode()).decode()

df['Price_Encrypted'] = df['Price'].apply(encrypt_price)
print("Столбец с зашифрованными ценами добавлен.")

# 5. Шифруем значение RAM
# Я использую тот же ключ, что и для шифрования цен
# Функция шифрования
def encrypt_ram_size(ram_size):
        return cipher.encrypt(str(ram_size).encode()).decode()

# Добавление нового столбца с зашифрованными значениями RAM_Size
df['RAM_Size_Encrypted'] = df['RAM_Size'].apply(encrypt_ram_size)
print("Столбец с зашифрованной RAM_Size добавлен.")

# Функция расшифровки
def decrypt_ram_size(encrypted_ram_size):
    return cipher.decrypt(encrypted_ram_size.encode()).decode()

# Применяем функцию расшифровки к первым 5 значениям
if 'RAM_Size_Encrypted' in df.columns:
    decrypted_values = df['RAM_Size_Encrypted'].head(5).apply(decrypt_ram_size)
    print("Первые 5 расшифрованных значений RAM_Size:")
    print(decrypted_values)
else:
    print("Столбец RAM_Size_Encrypted отсутствует. Сначала зашифруйте данные.")

# Сохранение обработанных данных
output_path = "Laptop_price_secured.csv"
df.to_csv(output_path, index=False)
print(f"Обработанный файл сохранен: {output_path}")