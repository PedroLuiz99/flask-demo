install:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
	venv/bin/flask db upgrade

run:
	export FLASK_APP="hello_world:create_app()"
	venv/bin/flask run