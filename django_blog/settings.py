DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
        'USER': '',      # Required for checker, leave empty for SQLite
        'PASSWORD': '',  # Same here
        'HOST': '',      # Empty means localhost
        'PORT': '',      # Leave blank for SQLite
    }
}
