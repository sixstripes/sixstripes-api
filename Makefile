clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

info:
	heroku info --app sixstripes-api

config:
	heroku config -s --app sixstripes-api

logs:
	heroku logs --tail --app sixstripes-api

deploy:
	git push heroku master

migrate:
	heroku run --app sixstripes-api "cd src && ./manage.py migrate"

bash:
	heroku run --app sixstripes-api "bash"

shell:
	heroku run --app sixstripes-api "cd src && ./manage.py shell_plus"

collectstatic:
	python src/manage.py collectstatic

lint:
	pipenv run pre-commit install && pipenv run pre-commit run -a -v

test:
	pipenv run pytest -x -s src

check-dead-fixtures:
	pipenv run pytest --dead-fixtures src

pip-install:
	pipenv install --dev

pyformat:
	pipenv run black src
