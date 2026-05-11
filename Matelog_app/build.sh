python manage.py migrate
python manage.py collectstatic --noinput
gunicorn Matelog_app.wsgi:application
