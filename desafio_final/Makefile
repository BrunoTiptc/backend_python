run:
	@uvicorn main:app --reload

creat-migrations:
    @PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "$(d)"

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head
	