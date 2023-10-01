# permissions.py

def es_admin(user):
    return user.is_authenticated and user.is_superuser
