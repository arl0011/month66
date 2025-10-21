def save_google_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        user.first_name = response.get('given_name', '')
        user.last_name = response.get('family_name', '')
        user.registration_source = 'google'
        user.is_active = True

        # last_login обновляется автоматически при входе
        # Если хочешь явно записать дату создания:
        if not user.date_joined:
            from django.utils.timezone import now
            user.date_joined = now()

        user.save()
