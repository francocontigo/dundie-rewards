.PHONY: install virtualenv ipython clean test pflake8 black build


install:
	@echo "Installing for dev environment"
	@venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@venv/bin/python -m pip -m venv .venv


ipython:
	@venv/bin/ipython

fmt:
	@venv/bin/black dundie tests integration

lint:
	@venv/bin/pflake8

test:
	@venv/bin/pytest -vv -s --forked

testci:
	@venv/bin/pytest -vv -v --junitxml=test-result.xml --forked

watch:
	.venv/bin/ptw -- -vv -s

clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

build:
	@python setup.py sdist bdist_wheel
