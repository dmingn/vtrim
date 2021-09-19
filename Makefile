PACKAGE_NAME = vtrim

setup.py: pyproject.toml poetry.lock src/*
	poetry build
	tar zxvf dist/$(PACKAGE_NAME)-*.tar.gz -C ./dist
	cp dist/$(PACKAGE_NAME)-*/setup.py setup.py
	rm -rf dist
	poetry run black setup.py
