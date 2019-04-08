# poc_flask_gcp
Poc for testing flaks on GCP With connexion and SQL Alchemy

# Install dependencies
`pipenv install`

# Local ENV
`cp .env.example .env`
`export env $(cat .env)`

# Run migrations
`alembic upgrade head`

# Create initial seed
`pipenv run python manage.py seed`

# Run app
`pipenv run python manage.py runserver`
