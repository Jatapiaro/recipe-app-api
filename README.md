# recipe-app-api

1. Create your Dockerfile
2. docker build .
3. Create your docker-composer.yml file
4. docker-composer build

## Create the django project
`docker-compose run app sh -c "django-admin.py startproject app ."`
`docker-compose run app sh -c "django-admin.py startproject core"`

# Run the tests
`docker-compose run app sh -c "python manage.py test && flake8"`
