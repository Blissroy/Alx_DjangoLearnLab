# django_blog/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': '',      # Add this line (empty string for SQLite)
        'PASSWORD': '',  # Add this line (optional but good practice)
        'HOST': '',      # Add this line (optional)
        'PORT': '',      # Add this line (empty string for SQLite)
    }
}
