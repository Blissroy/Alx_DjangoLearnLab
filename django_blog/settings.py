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
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ... other settings ...

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ... other settings ...
