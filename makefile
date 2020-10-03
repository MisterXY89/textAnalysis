freeze:
	@echo "Updating requirements:"
	@pip freeze | grep -v "pkg-resources\|de-core-news-sm"  > requirements.txt
	@echo "https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-2.3.0/de_core_news_sm-2.3.0.tar.gz" >> requirements.txt

deploy:
	@echo "Starting deployment - via docker container push:"
	@heroku container:push web –app zeitung-plus

clean:
	@echo "Cleaning project:"
	@py3clean .

test:
	@echo "Testing:"
	@python -m pytest test.py

lint:
	@echo "Linting:"
	@python -m pylint app.py API.py


run:
	flask run

docker-build:
	@echo "Building docker file:"
	docker build -t flask-heroku:latest .

docker-run:
	@echo "Running docker:"
	docker run -d -p 5000:5000 flask-heroku

docker-id:
	@docker ps | sed -n 2p | cut -f 1 -d " "
