SECRET_KEY = '8452590h2tn935t8y3gub234'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'freegeek',
        'HOST': 'db',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}


DEBUG=True