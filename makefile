freeze:
	@echo "Updating requirements:"
	pip freeze | grep -v "pkg-resources" > requirements.txt

deploy:
	@echo "Starting deployment:"

clean:
	@echo "Cleaning project via"
	py3clean .

run:
	flask run