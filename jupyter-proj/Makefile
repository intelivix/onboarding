# Makefile onboarding

# These targets are not files

.PHONY: all help clean pep8 test test.dev test.failfirst test.collect test.skip.covered

all: help

help:
	@echo 'Makefile *** onboarding *** Makefile'

check.test_path:
	@if test "$(TEST_PATH)" = "" ; then echo "TEST_PATH is undefined. The default is tests."; fi

clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

pep8:
	@pycodestyle --filename="*.py" .

### TESTS

test: check.test_path
	@py.test -s $(TEST_PATH) --cov --cov-report term-missing --basetemp=tests/media --disable-pytest-warnings

test.dev: check.test_path
	@py.test -s $(TEST_PATH) --cov --cov-fail-under 70 --cov-report term-missing --basetemp=tests/media --disable-pytest-warnings

test.failfirst: check.test_path
	@py.test -s -x $(TEST_PATH) --basetemp=tests/media --disable-pytest-warnings

test.collect: check.test_path
	@py.test -s $(TEST_PATH) --basetemp=tests/media --collect-only --disable-pytest-warnings

test.skip.covered: check.test_path
	@py.test -s $(TEST_PATH) --cov --cov-report term:skip-covered --doctest-modules --basetemp=tests/media --disable-pytest-warnings
