from django.core.cache import cache
import random

def save_code(user_id):
    code = str(random.randint(100000, 999999))
    cache.set(f"code:{user_id}", code, timeout=300)  # хранится 5 минут
    return code

def check_code(user_id, entered_code):
    key = f"code:{user_id}"
    code = cache.get(key)
    if code == entered_code:
        cache.delete(key)  # удаляем после проверки
        return True
    return False
