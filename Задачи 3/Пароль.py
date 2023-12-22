def check_password_strength(password):
    conditions = {
        'length': len(password) >= 8,
        'uppercase': any(char.isupper() for char in password),
        'lowercase': any(char.islower() for char in password),
        'digits': any(char.isdigit() for char in password),
        'special_chars': any(not char.isalnum() for char in password)
    }

    strength = sum(conditions.values())
    return strength

# Пример использования:
user_password = "MyP@ssw0rd"
strength = check_password_strength(user_password)
print(f"Сложность пароля: {strength}")
