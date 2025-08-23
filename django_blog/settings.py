DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.sqlite3',
        "NAME": BASE_DIR / "db.sqlite3",
        "USER": '',       # Required key (even if unused in SQLite)
        'PASSWORD': '',   # Required key
        "HOST": 'localhost',  # Explicit for clarity
        "PORT": '',       # Required key
    }
}
