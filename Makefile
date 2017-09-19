NAMESPACE=llimllib
APP=fabulous

.PHONY: testall
testall: requirements
	tox

# to run a single file, with debugger support:
# pytest -s test/test_plugins/test_image.py
.PHONY: test
test: install
	LANG=en_US.UTF-8 pytest --cov=fabulous --cov-report term-missing

.PHONY: clean
clean:
	rm -rf build dist fabulous.egg-info

.PHONY: run
run: install
	sudo bin/fabulous

.PHONY: repl
repl: install
	sudo bin/fabulous -t

.PHONY: requirements
requirements:
	sudo -H pip install -r requirements.txt

.PHONY: install
install: requirements
	python setup.py install
	make clean

.PHONY: publish
publish:
	pandoc -s -w rst README.md -o README.rst
	python setup.py sdist upload
	rm README.rst

.PHONY: flake8
flake8:
	flake8 fabulous test
