all: clean-pyc test

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

test:
	@python -m unittest discover -p '*_test.py'

requirements:
	@pip install -r requirements.txt --use-mirrors

install: requirements
	python setup.py install
