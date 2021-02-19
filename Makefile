port = sudo lsof --t -i:5432

create-db:
	sudo kill -9 $(port)
	docker-compose up -d --force-recreate
delete-db:
	docker-compose down -v
runserver:
	poetry run uvicorn quiero_trabajar_demo.asgi:app --reload
init-migrations:
	poetry run alembic init migrations
migrate:
ifdef m
	poetry run alembic revision --autogenerate -m "$(m)"
else
	echo "ERROR: add a message - make migrate m='message'"
endif
upgrade:
	poetry run alembic upgrade head
downgrade:
	poetry run alembic downgrade -1
stamp:
	poetry run alembic stamp head
