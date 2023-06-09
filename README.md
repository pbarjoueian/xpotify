# Xpotify

* ## Manual Documentation

* ## Local Deployment Using Docker

    1. Get a valid `.env` from your team lead and put inside the project directory and modify it with your preferred configurations.
    2. You can use `docker-compose -f docker-compose.dev.yml up postgres` up to start with minimum dependencies
    3. create and activate a python virtualenv
       1. create a python virtualenv using `python -m venv venv`
       2. activate virtualenv using `venv\Scripts\activate`
    4. run `pip install pip -U` inside your virtualenv
    5. run `pip install pipenv` inside your virtualenv
    6. run `pipenv install -d` inside your virtualenv
    7. run `python manage.py migrate`
    8. run `python manage.py fake_admin` _will create_ (email=<admin@test.com>, password=123456789)
    9. run `python manage.py fake_user` _will create_ (email=<user@test.com>, password=123456789)
    10. run `python manage.py import_initial_data --path tracks/management/commands/sample_tracks.csv`
    11. run `python manage.py runserver

* ## Note

  * For development and maintenance please install git hooks using: `pre-commit install`
  * Swagger Address: `{BASE_URL}/api/schema/swagger-ui/`

* ## TODOs

  * [x] Add separated Docker files for production and development environments
  * [x] Make Docker images smaller
  * [x] Change login to jwt
  * [x] Add production configurations
  * [x] Disable rest_registration login API
  * [x] Use separated models and relations for Model objects
  * [x] Use a more efficient and distributed approach for training
  * [x] Select rows in chunks
  * [x] Add logging and APM
  * [x] Add throttling configurations
  * [x] Improve Redis usage
