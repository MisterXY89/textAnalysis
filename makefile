freeze:
	@echo "Updating requirements:"
	pip freeze | grep -v "pkg-resources" > requirements.txt

deploy:
	@echo "Starting deployment:"
	git push heroku master

clean:
	@echo "Cleaning project via"
	py3clean .

test:
	@echo "Testing"
	python -m pytest test.py

lint:
	@echo "Linting:"
	python -m pylint app.py API.py


run:
	flask run
