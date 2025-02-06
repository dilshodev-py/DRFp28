mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser


udb:
	rm -rf apps/migrations/*
	touch apps/migrations/__init__.py
	rm -rf db.sqlite3
	python3 manage.py makemigrations
	python3 manage.py migrate
