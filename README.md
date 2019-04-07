# poc_flask_gcp
Poc for testing flaks on GCP With connexion and SQL Alchemy

# Run migrations
cp example.env .env
`alembic upgrade head`

# Create initial seed
`python manage.py seed`

# Run app
`python manage.py runserver`
