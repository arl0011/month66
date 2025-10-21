from rest_framework.exceptions import ValidationError
from datetime import date, datetime


def validate_user_age(birthdate_str):
    """
    Проверяет возраст пользователя по строке birthdate в формате ISO (YYYY-MM-DD).
    Если дата отсутствует или возраст < 18 — выбрасывает ValidationError.
    """
    if not birthdate_str:
        raise ValidationError("Укажите дату рождения, чтобы создать продукт.")

    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError("Неверный формат даты рождения.")

    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")
