
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "e20d1399-3214-43c4-b3a1-bc57043004dd99398300-d1fe-4cd8-a886-39699cf5444db83fa3a6-905f-4251-a02d-758785f13f31"
NEVERCACHE_KEY = "c6da6a2f-5113-4f17-930a-570f75c7567d77b348cc-ce9e-4b11-a435-58ecdcda021c61126e1b-ecb5-4f62-8d1f-d65e9cc7f0e8"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "cerealbox",
        # Not used with sqlite3.
        "USER": "admin",
        # Not used with sqlite3.
        "PASSWORD": "TobDiob7",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
