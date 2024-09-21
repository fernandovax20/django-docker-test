docker-compose -f docker-compose.dev.yml exec web python manage.py collectstatic --noinput

 docker-compose -f docker-compose.dev.yml up --build

 