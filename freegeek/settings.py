"""Django settings for hackor project.
For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
To set up a new system:
    sudo adduser --no-create-home hackor  # use the password below?
    sudo su postgresql
    psql -d template1 -U postgres
    template1=# CREATE USER hackor WITH PASSWORD 'aisolvesnphardproblemsapproximately';
    CREATE ROLE
    template1=# CREATE DATABASE hackor;
    CREATE DATABASE
    template1=# GRANT ALL PRIVILEGES ON DATABASE hackor to hackor;
    GRANT
    template1=# \q
To restore a pg_dump
    sudo su hackor
    pg_restore -U hackor -d hackor /tmp/pg_dump_hackor.psqlc
or
    sudo su postgres
    pg_restore -U postgres -d hackor /tmp/pg_dump_hackor.psqlc
To runserver, don't forget the --insecure flag so that admin interface css/js can load!
    python manage.py runserver --insecure
"""
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = r'u-jpod4cx*q67vcp-ewnk3u$hm_1jo_*xqx9u1x-pg3-y3%kcd'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hackor',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'hackor',
        'PASSWORD': 'aisolvesnphardproblemsapproximately',
    },
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'twitterbot/tweets.db',
    }
}
DEBUG = True
