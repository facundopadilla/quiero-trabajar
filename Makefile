create-db:
	docker-compose up -d --force-recreate
delete-db:
	docker rm -fv $(docker ps -aq)
	docker-compose down -v
runserver:
	poetry run uvicorn quiero_trabajar_demo.asgi:app --reload
init-migrations:
	poetry run alembic init migrations
migrate:
	poetry run alembic revision --autogenerate -m "$(msg)"
upgrade:
	poetry run alembic upgrade head
