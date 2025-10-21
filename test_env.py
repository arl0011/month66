from decouple import config

print("SECRET:", config('SECRET'))
print("GOOGLE KEY:", config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'))
print("GOOGLE SECRET:", config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'))
print("DEBUG:", config('DEBUG'))
