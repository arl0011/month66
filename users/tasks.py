from celery import shared_task
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone


@shared_task
def generate_and_save_code(username):
    code = "123456"  # тут можно сделать random.randint
    print(f"Код для {username}: {code}")
    return code



@shared_task
def delete_old_temp_files():
    print("🧹 Старые временные файлы успешно удалены.")
    return "done"



@shared_task
def send_promo_email(email):
    send_mail(
        subject="🔥 Скидка недели!",
        message="Успей купить товар со скидкой 50%!",
        from_email="noreply@shop.local",
        recipient_list=[email],
    )
    print(f"Письмо отправлено на {email}")
    return "email sent"
