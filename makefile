freeze:
	@echo "Updating requirements:"
	pip freeze | grep -v "pkg-resources\|de-core-news-sm"  > requirements.txt
	echo "https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-2.3.0/de_core_news_sm-2.3.0.tar.gz" >> requirements.txt

deploy:
	@echo "Starting deployment:"
	git push heroku master

clean:
	@echo "Cleaning project via"
	rm -r __pycache__/
	py3clean .

test:
	@echo "Testing"
	python -m pytest test.py

lint:
	@echo "Linting:"
	python -m pylint app.py API.py


run:
	flask run
